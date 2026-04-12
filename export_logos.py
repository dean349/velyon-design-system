import sys
import subprocess
import time

def install_playwright():
    try:
        import playwright
        print("Playwright already installed.")
    except ImportError:
        print("Installing Playwright...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])

def export():
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        print("Launching headless browser...")
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=4) # 4x resolution for high quality
        
        url = "file:///c:/ANTIGRAVITY PROJECTS/VELYON - LEGAL COMMAND CENTER/los-romeros-logo.html"
        print(f"Loading {url}")
        page.goto(url, wait_until="networkidle")
        
        # Give it a tiny bit extra time to ensure Google Fonts render completely
        page.wait_for_timeout(2000) 
        
        out_png = "c:/ANTIGRAVITY PROJECTS/VELYON - LEGAL COMMAND CENTER/Los_Romeros_Logo.png"
        out_jpg = "c:/ANTIGRAVITY PROJECTS/VELYON - LEGAL COMMAND CENTER/Los_Romeros_Logo.jpeg"
        
        locator = page.locator("section").nth(0).locator("div.bg-white")
        
        print(f"Saving PNG to {out_png}")
        locator.screenshot(path=out_png, omit_background=True)
        
        print(f"Saving JPEG to {out_jpg}")
        locator.screenshot(path=out_jpg, type="jpeg", quality=100)
        
        # Let's also do the dark mode logo
        out_dark_png = "c:/ANTIGRAVITY PROJECTS/VELYON - LEGAL COMMAND CENTER/Los_Romeros_Logo_Dark.png"
        out_dark_jpg = "c:/ANTIGRAVITY PROJECTS/VELYON - LEGAL COMMAND CENTER/Los_Romeros_Logo_Dark.jpeg"
        
        dark_locator = page.locator("section").nth(1).locator("div.bg-slate-900")
        
        print(f"Saving Dark PNG to {out_dark_png}")
        dark_locator.screenshot(path=out_dark_png, omit_background=True)
        
        print(f"Saving Dark JPEG to {out_dark_jpg}")
        dark_locator.screenshot(path=out_dark_jpg, type="jpeg", quality=100)

        browser.close()
        print("Export completed successfully!")

if __name__ == "__main__":
    install_playwright()
    export()
