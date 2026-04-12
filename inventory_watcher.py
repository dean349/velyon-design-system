"""
================================================================================
  VELYON FORENSIC VAULT SYNC ENGINE  v3.0
  inventory_watcher.py
================================================================================
  Watches D:\\VELYON - LEGAL COMMAND CENTER for file changes and syncs
  important case documents to:
    - gs://velyon-forensic-vault-dean/velyon/Los_Romeros_Case_Files/
    - GitHub: dean349/dean349.github.io

  Case folder routing maps local sub-folders → GCS case folders automatically.
  Brain/session files are EXCLUDED (not synced to save storage costs).
================================================================================
"""

import os
import sys
import time
import logging
import subprocess
import fnmatch
from pathlib import Path
from datetime import datetime

try:
    from watchdog.observers import Observer
    from watchdog.events import PatternMatchingEventHandler
except ImportError:
    print("ERROR: watchdog not installed. Run: pip install watchdog")
    sys.exit(1)

# ─── CONFIGURATION ────────────────────────────────────────────────────────────

# Use current script directory as base — works on Windows AND Cloud Workstation
BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

GCS_BUCKET  = "gs://velyon-forensic-vault-dean"
GCS_BASE    = f"{GCS_BUCKET}/velyon/Los_Romeros_Case_Files"

LOG_FILE    = BASE_DIR / "inventory_watcher.log"
REGISTRY    = BASE_DIR / "files_registry.json"

# Minimum seconds between sync operations (debounce)
SYNC_DEBOUNCE_SECS = 10

# ─── CASE FOLDER ROUTING MAP ──────────────────────────────────────────────────
# Maps: local subfolder name keyword → GCS case folder name
# First matching rule wins. Case-insensitive.

FOLDER_ROUTING = [
    # Local keyword fragment           → GCS folder
    ("brand identity",                  "01_Brand_Identity"),
    ("subsidiaries",                    "02_Wincham_Subsidiaries_Research"),
    ("wincham international",           "02_Wincham_Subsidiaries_Research"),
    ("scheme claim",                    "03_Wincham_Scheme_Claim_Master"),
    ("master file",                     "03_Wincham_Scheme_Claim_Master"),
    ("ssl forensic",                    "04_Wincham_SSL_Forensic_Audit"),
    ("property sale",                   "05_Property_Sale_Documents"),
    ("modelo 210",                      "06_Modelo_210_Spanish_CGT"),
    ("spanish cgt",                     "06_Modelo_210_Spanish_CGT"),
    ("legal claim",                     "07_Harrison_v_Wincham_Legal_Claim"),
    ("harrison vs",                     "07_Harrison_v_Wincham_Legal_Claim"),
    ("harrison v ",                     "07_Harrison_v_Wincham_Legal_Claim"),
    ("annual accounts",                 "08_Annual_Accounts_Companies_House"),
    ("companies house",                 "08_Annual_Accounts_Companies_House"),
    ("lanzarote",                       "09_Lanzarote_Financial_Breakdown"),
    ("financial breakdown",             "09_Lanzarote_Financial_Breakdown"),
    ("communication log",               "10_Communication_Logs"),
    ("phil harrison",                   "10_Communication_Logs"),
    ("glo docs",                        "11_Wincham_Scheme_GLO_Docs"),
    ("glo ",                            "11_Wincham_Scheme_GLO_Docs"),
    ("mvl",                             "12_MVL_HMRC_Docs"),
    ("hmrc",                            "12_MVL_HMRC_Docs"),
    ("estate planning",                 "13_Estate_Planning_Info"),
    ("los romeros",                     "05_Property_Sale_Documents"),   # fallback
    ("wincham",                         "03_Wincham_Scheme_Claim_Master"), # fallback
]

# ─── IMPORTANT FILE EXTENSIONS ────────────────────────────────────────────────
# Only sync these types. Everything else ignored.
IMPORTANT_EXTENSIONS = {
    ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".csv",
    ".msg", ".eml", ".txt", ".rtf", ".odt", ".ods",
    ".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".webp",
    ".mp4", ".mov", ".avi", ".mkv",
    ".mp3", ".m4a", ".wav",
    ".zip", ".7z", ".tar", ".gz",
    ".pptx", ".ppt",
    ".html", ".htm",  # For important saved web pages in case folders
}

# ─── PATTERNS TO IGNORE ───────────────────────────────────────────────────────
# These patterns are checked against the full file path (lowercase)
IGNORE_PATTERNS = [
    # This script's own output files
    "*inventory_watcher.log*",
    "*files_registry.json*",
    "*inventory_watcher.py*",

    # Git internals
    "*\\.git\\*",
    "*/.git/*",
    "*.git*",

    # Nested git repositories
    "*_github_los_romeros_repo*",
    "*_github_*",

    # VS Code / IDE
    "*\\.vscode\\*",
    "*/.vscode/*",
    "*.code-workspace*",

    # Antigravity brain files (NOT synced to vault - saves storage costs)
    "*antigravity\\brain*",
    "*antigravity/brain*",
    "*\\.gemini\\antigravity*",
    "*/.gemini/antigravity*",

    # Node / Python
    "*node_modules*",
    "*__pycache__*",
    "*.pyc",
    "*.pyo",

    # Temp / system
    "*.tmp",
    "*.temp",
    "~$*",
    "*.DS_Store",
    "thumbs.db",
    "desktop.ini",

    # The landing page index (managed separately)
    "*antigravity_files_produced*",
    "*index.html",
]

# ─── LOGGING SETUP ────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
)
log = logging.getLogger("VelyonVaultSync")


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def is_ignored(file_path: str) -> bool:
    """Return True if this file should be skipped."""
    fp_lower = file_path.lower().replace("/", "\\")
    for pattern in IGNORE_PATTERNS:
        if fnmatch.fnmatch(fp_lower, pattern.lower()):
            return True
    return False


def is_important_file(file_path: str) -> bool:
    """Return True only for document/evidence file types we care about."""
    ext = Path(file_path).suffix.lower()
    return ext in IMPORTANT_EXTENSIONS


def get_gcs_folder(file_path: str) -> str:
    """
    Determine which GCS case folder this file belongs to.
    Inspects the full path for known folder keywords.
    Returns GCS folder name, or None if file should not be synced.
    """
    path_lower = file_path.lower()

    for keyword, gcs_folder in FOLDER_ROUTING:
        if keyword.lower() in path_lower:
            return gcs_folder

    # File is in base dir or unrecognised subfolder — skip unless in a named case folder
    return None


def sync_file_to_gcs(local_path: str):
    """Upload a single file to the correct GCS case folder."""
    if is_ignored(local_path):
        log.debug(f"IGNORED: {local_path}")
        return

    if not is_important_file(local_path):
        log.debug(f"NOT IMPORTANT TYPE: {local_path}")
        return

    if not os.path.isfile(local_path):
        log.debug(f"NOT A FILE (skipping): {local_path}")
        return

    gcs_folder = get_gcs_folder(local_path)
    if gcs_folder is None:
        log.debug(f"NO GCS ROUTING MATCH: {local_path}")
        return

    filename = os.path.basename(local_path)
    gcs_dest = f"{GCS_BASE}/{gcs_folder}/{filename}"

    log.info(f"SYNCING → {gcs_folder}: {filename}")
    try:
        result = subprocess.run(
            ["gcloud", "storage", "cp", local_path, gcs_dest],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0:
            log.info(f"✅ UPLOADED: {filename} → {gcs_folder}")
        else:
            log.error(f"❌ UPLOAD FAILED: {filename}\n{result.stderr.strip()}")
    except subprocess.TimeoutExpired:
        log.error(f"⏱ TIMEOUT uploading: {filename}")
    except FileNotFoundError:
        log.error("❌ 'gcloud' not found in PATH. Is Google Cloud SDK installed?")


def run_git_sync():
    """Commit and push any tracked changes to GitHub (safe — won't crash on nested repos)."""
    try:
        # Stage only tracked files — avoids nested repo issues
        result = subprocess.run(
            ["git", "add", "-u"],
            cwd=str(BASE_DIR), capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            log.warning(f"git add -u warning: {result.stderr.strip()}")
            return

        # Check if there's anything to commit
        status = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=str(BASE_DIR), capture_output=True, timeout=30
        )
        if status.returncode == 0:
            log.debug("Git: nothing to commit.")
            return

        # Commit
        commit_msg = f"Auto-sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=str(BASE_DIR), capture_output=True, text=True, timeout=30
        )

        # Push
        push = subprocess.run(
            ["git", "push"],
            cwd=str(BASE_DIR), capture_output=True, text=True, timeout=60
        )
        if push.returncode == 0:
            log.info("✅ Git push complete.")
        else:
            log.warning(f"Git push warning: {push.stderr.strip()}")

    except subprocess.TimeoutExpired:
        log.error("⏱ Git operation timed out.")
    except Exception as e:
        log.error(f"❌ Git sync error: {e}")


# ─── FILE SYSTEM EVENT HANDLER ────────────────────────────────────────────────

class VaultSyncHandler(PatternMatchingEventHandler):
    """Watchdog handler — only fires on important file types, ignores own logs."""

    def __init__(self):
        # Only watch these extensions at the watchdog level
        patterns = [f"*{ext}" for ext in IMPORTANT_EXTENSIONS]
        ignore_patterns = [
            "*.log", "*.json", "*.py",
            f"*{LOG_FILE.name}*",
            f"*{REGISTRY.name}*",
        ]
        super().__init__(
            patterns=patterns,
            ignore_patterns=ignore_patterns,
            ignore_directories=True,
            case_sensitive=False,
        )
        self._last_sync = 0

    def _debounced_sync(self, path):
        """Prevent rapid-fire syncs within SYNC_DEBOUNCE_SECS."""
        now = time.time()
        if now - self._last_sync < SYNC_DEBOUNCE_SECS:
            log.debug(f"Debounced: {path}")
            return
        self._last_sync = now
        sync_file_to_gcs(path)
        run_git_sync()

    def on_created(self, event):
        log.info(f"NEW FILE: {event.src_path}")
        self._debounced_sync(event.src_path)

    def on_modified(self, event):
        log.info(f"MODIFIED: {event.src_path}")
        self._debounced_sync(event.src_path)

    def on_moved(self, event):
        log.info(f"MOVED → {event.dest_path}")
        self._debounced_sync(event.dest_path)


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    log.info("=" * 60)
    log.info("  VELYON FORENSIC VAULT SYNC ENGINE v3.0 — STARTING")
    log.info(f"  Watching: {BASE_DIR}")
    log.info(f"  GCS Vault: {GCS_BASE}")
    log.info("=" * 60)

    handler  = VaultSyncHandler()
    observer = Observer()
    observer.schedule(handler, str(BASE_DIR), recursive=True)
    observer.start()

    log.info("🟢 Watcher active. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("🔴 Stopping watcher...")
        observer.stop()

    observer.join()
    log.info("Vault sync engine stopped.")


if __name__ == "__main__":
    main()