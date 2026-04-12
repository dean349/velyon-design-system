"""
Generate Antigravity_Files_Produced_Last_48hrs.pdf
Uses reportlab for a professional, well-formatted output.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

OUTPUT = r"C:\ANTIGRAVITY PROJECTS\VELYON - LEGAL COMMAND CENTER\Antigravity_Files_Produced_Last_48hrs.pdf"

# ─── COLOURS ───────────────────────────────────────────────────────────────
BG        = colors.HexColor("#0d0f14")
SURFACE   = colors.HexColor("#13161e")
CARD      = colors.HexColor("#1a1e2a")
BORDER    = colors.HexColor("#252a38")
TEXT      = colors.HexColor("#e2e8f0")
MUTED     = colors.HexColor("#8b95aa")
ACCENT    = colors.HexColor("#6c63ff")
ACCENT2   = colors.HexColor("#a78bfa")
GREEN     = colors.HexColor("#22d3a0")
RED       = colors.HexColor("#f87171")
AMBER     = colors.HexColor("#fbbf24")
BLUE      = colors.HexColor("#60a5fa")
PINK      = colors.HexColor("#f472b6")
CYAN      = colors.HexColor("#22d3ee")
ORANGE    = colors.HexColor("#fb923c")
WHITE     = colors.white
ROW_EVEN  = colors.HexColor("#13161e")
ROW_ODD   = colors.HexColor("#1a1e2a")

FMT_COLORS = {
    ".md":   BLUE,
    ".html": RED,
    ".png":  GREEN,
    ".jpeg": GREEN,
    ".webp": ACCENT2,
    ".pdf":  ORANGE,
    ".mp4":  PINK,
    ".docx": CYAN,
    ".py":   colors.HexColor("#a3e635"),
    ".json": AMBER,
}

# ─── STYLES ────────────────────────────────────────────────────────────────
def build_styles():
    base = {
        "fontName": "Helvetica",
        "textColor": TEXT,
        "backColor": BG,
    }
    return {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=20,
                                textColor=WHITE, spaceAfter=2),
        "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=10,
                                   textColor=MUTED, spaceAfter=8),
        "section_label": ParagraphStyle("sl", fontName="Helvetica-Bold", fontSize=8,
                                        textColor=MUTED, spaceBefore=14, spaceAfter=6,
                                        letterSpacing=1.5),
        "section_head": ParagraphStyle("sh", fontName="Helvetica-Bold", fontSize=11,
                                       textColor=WHITE, spaceBefore=4, spaceAfter=2),
        "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=8,
                               textColor=TEXT, leading=11),
        "cell_mono": ParagraphStyle("cm", fontName="Courier", fontSize=7.5,
                                    textColor=TEXT, leading=10),
        "cell_muted": ParagraphStyle("cmu", fontName="Helvetica", fontSize=8,
                                     textColor=MUTED, leading=11),
        "fmt": ParagraphStyle("fmt", fontName="Courier-Bold", fontSize=7,
                              leading=10),
        "footer": ParagraphStyle("footer", fontName="Helvetica", fontSize=7.5,
                                 textColor=MUTED, alignment=TA_CENTER),
        "stat_label": ParagraphStyle("stl", fontName="Helvetica-Bold", fontSize=8,
                                     textColor=MUTED, alignment=TA_CENTER),
        "stat_val":   ParagraphStyle("stv", fontName="Helvetica-Bold", fontSize=18,
                                     textColor=ACCENT2, alignment=TA_CENTER),
    }

# ─── SECTION COLOURS ───────────────────────────────────────────────────────
SECTION_COLORS = {
    "Wincham SSL Forensic Audit":               RED,
    "Los Romeros — Property Sale Documents":    ORANGE,
    "Los Romeros — Brand Identity":             AMBER,
    "Velyon — Brand & Design":                  ACCENT2,
    "Velyon — Marketing Dashboard & PRD":       BLUE,
    "Prompts & Tooling":                        CYAN,
    "Wincham SSL — Brain Artifacts":            RED,
    "Los Romeros Brand — Brain Artifacts":      AMBER,
    "Velyon Brand — Brain Artifacts":           ACCENT2,
    "Velyon Marketing — Brain Images":          BLUE,
    "Velyon PRD — Brain Artifacts":             CYAN,
    "Google Cloud Setup — Brain Assets":        GREEN,
}

# ─── DATA ──────────────────────────────────────────────────────────────────
SECTIONS = [
    {
        "group": "WORKSPACE FILES",
        "path": r"C:\ANTIGRAVITY PROJECTS\VELYON - LEGAL COMMAND CENTER\ ",
        "items": [
            ("Wincham SSL Forensic Audit", RED, [
                (1,  "WINCHAM_SSL_BREACH_FULL_REPORT",               ".md",   "23 KB"),
                (2,  "Wincham SSL Breach / WINCHAM_SSL_BREACH_FULL_REPORT", ".md", "33 KB"),
                (3,  "Wincham SSL Breach / WINCHAM_MASTER_REPORT_WITH_EVIDENCE", ".md", "—"),
                (4,  "evidence / adremaccs_cert_details",             ".png",  "65 KB"),
                (5,  "evidence / adremaccs_com_home",                 ".png",  "237 KB"),
                (6,  "evidence / adremaccs_homepage_ssl_status",      ".png",  "243 KB"),
                (7,  "evidence / adremaccs_ssllabs_report",           ".png",  "52 KB"),
                (8,  "evidence / wincham_com_cert_details",           ".png",  "66 KB"),
                (9,  "evidence / wincham_es_dns_error",               ".png",  "32 KB"),
                (10, "evidence / wincham_homepage_ssl_status",        ".png",  "444 KB"),
                (11, "evidence / wincham_ssl_audit_all_sites",        ".webp", "12 KB"),
                (12, "evidence / wincham_ssllabs_report",             ".png",  "66 KB"),
                (13, "evidence / wincham_wayback_machine_calendar",   ".png",  "71 KB"),
                (14, "evidence / winchamgroup_com_dns_error",         ".png",  "32 KB"),
                (15, "evidence / winchamiht_com_error",               ".png",  "34 KB"),
                (16, "evidence / winchamiht_error_page",              ".png",  "34 KB"),
                (17, "evidence / winchamiht_failed_assessment",       ".png",  "102 KB"),
                (18, "evidence / winchampropertyshop_com_home",       ".png",  "245 KB"),
                (19, "evidence / winchampropertyshop_homepage_ssl_status", ".png", "566 KB"),
                (20, "evidence / winchampropertyshop_ssllabs_report", ".png",  "69 KB"),
                (21, "evidence / winchamukcompany_cert_details",      ".png",  "67 KB"),
                (22, "evidence / winchamukcompany_com_home",          ".png",  "690 KB"),
                (23, "evidence / winchamukcompany_homepage_ssl_status", ".png","688 KB"),
                (24, "evidence / winchamukcompany_ssllabs_report",    ".png",  "67 KB"),
            ]),
            ("Los Romeros — Property Sale Documents", ORANGE, [
                (25, "Completion_Statement",                           ".html", "—"),
                (26, "1. The_Wincham_Scheme_Fraud_Overview_video_1",  ".mp4",  "39 MB"),
                (27, "2. WINCHAM_SCHEME_SIC_CODE-MISCLASIFICATION",   ".mp4",  "55 MB"),
                (28, "3. The_Wincham_Indictment",                     ".mp4",  "59 MB"),
                (29, "4. LOS_ROMOEROS — WINCHAM — CLOSING_COSTS",     ".mp4",  "29 MB"),
                (30, "5. LOS_ROMOEROS — WINCHAM — OVERVIEW_VIDEO_2",  ".mp4",  "57 MB"),
                (31, "6. Los_Romores_Transaction_Audit (1)",          ".pdf",  "9 MB"),
                (32, "Los Romeros Ltd — Lanzarote Property Sale Full Financial Breakdown", ".pdf", "1.9 MB"),
                (33, "Transaction_Audit_and_Capital_Transition",       ".pdf",  "13 MB"),
                (34, "Web Pages Velyon — Phil Harrison Claims Against Wincham", ".pdf", "123 KB"),
                (35, "Wincham_Fraud_Exposed v2",                      ".pdf",  "9.9 MB"),
                (36, "Wincham_Fraud_Exposed_PRESENTATION_TO_UK_CMC",  ".pdf",  "9.9 MB"),
                (37, "michael-harper",                                 ".pdf",  "234 KB"),
            ]),
            ("Los Romeros — Brand Identity", AMBER, [
                (38, "Los_Romeros_Brand_Guidelines",  ".md",   "3 KB"),
                (39, "Los_Romeros_Brand_Kit",         ".md",   "3 KB"),
                (40, "Los_Romeros_Brand_Style_Guide", ".md",   "4 KB"),
                (41, "Los_Romeros_Logo (light)",      ".jpeg", "252 KB"),
                (42, "Los_Romeros_Logo (light)",      ".png",  "299 KB"),
                (43, "Los_Romeros_Logo_Dark",         ".jpeg", "278 KB"),
                (44, "Los_Romeros_Logo_Dark",         ".png",  "306 KB"),
                (45, "los-romeros-logo",              ".html", "6 KB"),
                (46, "export_logos",                  ".py",   "—"),
                (47, "fix_encoding",                  ".py",   "—"),
            ]),
            ("Velyon — Brand & Design", ACCENT2, [
                (48, "Brand_Guidelines",     ".md",   "4 KB"),
                (49, "Brand_Kit",            ".md",   "3 KB"),
                (50, "Style_Guide",          ".md",   "4 KB"),
                (51, "Velyon_Design_System", ".html", "25 KB"),
            ]),
            ("Velyon — Marketing Dashboard & PRD", BLUE, [
                (52, "index (Marketing Dashboard)",                                ".html", "—"),
                (53, "VELYON - LEGAL COMMAND CENTER - PRODUCT REQUIREMENTS DOCUMENT (PRD)", ".docx", "202 KB"),
            ]),
            ("Prompts & Tooling", CYAN, [
                (54, "ultimate-html-builder-prompt",        ".md",   "6 KB"),
                (55, "docs / ultimate-html-builder-prompt", ".md",   "6 KB"),
                (56, "Ultimate_Prompt_Landing",             ".html", "53 KB"),
            ]),
        ]
    },
    {
        "group": "BRAIN FILES",
        "path": r"C:\Users\Dean Harrison\.gemini\antigravity\brain\ ",
        "items": [
            ("Wincham SSL — Brain Artifacts", RED, [
                (57, "WINCHAM_MASTER_INVESTIGATION_FILE",      ".md",   "108 KB"),
                (58, "WINCHAM_SSL_BREACH_FULL_REPORT",         ".md",   "23 KB"),
                (59, "WINCHAM_SSL_UPDATED_EVIDENCE_ADDENDUM",  ".md",   "17 KB"),
                (60, "wincham_investigation_report",           ".md",   "4 KB"),
                (61, "implementation_plan",                    ".md",   "6.5 KB"),
                (62, "task",                                   ".md",   "693 B"),
                (63, "wincham_ssl_screenshot_verify",          ".webp", "1 MB"),
                (64, "wincham_ssl_cert_dates",                 ".webp", "360 KB"),
                (65, "wincham_ssl_audit_all_sites",            ".webp", "12 KB"),
            ]),
            ("Los Romeros Brand — Brain Artifacts", AMBER, [
                (66, "implementation_plan",      ".md",  "4 KB"),
                (67, "task",                     ".md",  "361 B"),
                (68, "walkthrough",              ".md",  "3.3 KB"),
                (69, "los_romeros_icon (AI)",    ".png", "229 KB"),
            ]),
            ("Velyon Brand — Brain Artifacts", ACCENT2, [
                (70, "Brand_Guidelines",      ".md", "4.7 KB"),
                (71, "Brand_Kit",             ".md", "3.2 KB"),
                (72, "Style_Guide",           ".md", "4.1 KB"),
                (73, "implementation_plan",   ".md", "3.1 KB"),
            ]),
            ("Velyon Marketing — Brain Images", BLUE, [
                (74,  "diagram_revenue_multiplier",      ".png", "1.1 MB"),
                (75,  "diagram_unclog_pipeline",         ".png", "967 KB"),
                (76,  "diagram_remove_busywork",         ".png", "834 KB"),
                (77,  "diagram_revenue_funnel",          ".png", "870 KB"),
                (78,  "diagram_support_triage",          ".png", "1 MB"),
                (79,  "diagram_roi_gauge",               ".png", "519 KB"),
                (80,  "diagram_human_machine_symbiosis", ".png", "702 KB"),
                (81,  "diagram_break_bottleneck",        ".png", "829 KB"),
                (82,  "diagram_command_center_ui",       ".png", "667 KB"),
                (83,  "diagram_elevate_workforce",       ".png", "819 KB"),
                (84,  "diagram_data_mesh_network",       ".png", "975 KB"),
                (85,  "human_supply_chain",              ".png", "793 KB"),
                (86,  "human_customer_success",          ".png", "714 KB"),
                (87,  "human_operations_director",       ".png", "800 KB"),
                (88,  "human_strategic_boardroom",       ".png", "787 KB"),
                (89,  "human_executive_dashboard",       ".png", "727 KB"),
                (90,  "human_financial_analyst",         ".png", "753 KB"),
                (91,  "human_healthcare_admin",          ".png", "660 KB"),
                (92,  "human_legal_command",             ".png", "717 KB"),
                (93,  "human_manufacturing_leader",      ".png", "777 KB"),
                (94,  "human_sales_closer",              ".png", "827 KB"),
                (95,  "implementation_plan",             ".md",  "3 KB"),
                (96,  "task",                            ".md",  "475 B"),
            ]),
            ("Velyon PRD — Brain Artifacts", CYAN, [
                (97,  "VELYON_PRD_V2",       ".md", "18 KB"),
                (98,  "VELYON_PRD_V3",       ".md", "15 KB"),
                (99,  "VELYON_PRD_V4",       ".md", "37 KB"),
                (100, "VELYON_PRD_V5",       ".md", "40 KB"),
                (101, "VELYON_PRD_Part1",    ".md", "5 KB"),
                (102, "VELYON_PRD_Part2",    ".md", "4.4 KB"),
                (103, "VELYON_PRD_Part3",    ".md", "8.6 KB"),
                (104, "implementation_plan", ".md", "2.9 KB"),
            ]),
            ("Google Cloud Setup — Brain Assets", GREEN, [
                (105, "gcloud_sdk_download",         ".webp", "558 KB"),
                (106, "gcloud_install_page",          ".webp", "366 KB"),
                (107, "gcloud_sdk_windows_install",   ".png",  "274 KB"),
                (108, "installer_download_page",      ".png",  "20 KB"),
            ]),
        ]
    },
]

# ─── BUILD ─────────────────────────────────────────────────────────────────
def build_pdf():
    S = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=16*mm, rightMargin=16*mm, topMargin=14*mm, bottomMargin=14*mm,
        title="Files Produced — Last 48 Hours",
        author="Antigravity",
    )

    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(BG)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        # header bar
        canvas.setFillColor(SURFACE)
        canvas.rect(0, A4[1]-18*mm, A4[0], 18*mm, fill=1, stroke=0)
        canvas.setFont("Helvetica-Bold", 9)
        canvas.setFillColor(ACCENT2)
        canvas.drawString(16*mm, A4[1]-11*mm, "Files Produced — Last 48 Hours")
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(A4[0]-16*mm, A4[1]-11*mm, "VELYON Legal Command Center · Antigravity")
        # footer
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(MUTED)
        canvas.drawCentredString(A4[0]/2, 8*mm, f"Page {doc.page}  ·  10 April 2026  ·  Attorney-Client Privileged Work Product")
        canvas.restoreState()

    story = []

    # ── COVER BLOCK ──
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("FILES PRODUCED — LAST 48 HOURS", S["title"]))
    story.append(Paragraph("Period: 2026-04-08 → 2026-04-10  ·  As of: 09:59 EST", S["subtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER, spaceAfter=10))

    # Stats row
    stats = [
        ("111", "Total Files"),
        ("37",  ".md Docs"),
        ("44",  ".png Images"),
        ("8",   ".pdf Reports"),
        ("6",   ".html Pages"),
        ("5",   ".mp4 Videos"),
        ("6",   ".webp"),
        ("5",   "Other"),
    ]
    stat_rows = [[
        Table(
            [[Paragraph(v, S["stat_val"])], [Paragraph(k, S["stat_label"])]],
            colWidths=[21*mm], rowHeights=[9*mm, 5*mm],
            style=TableStyle([
                ("BACKGROUND", (0,0), (-1,-1), CARD),
                ("BOX", (0,0), (-1,-1), 0.5, BORDER),
                ("ROUNDEDCORNERS", [4,4,4,4]),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ])
        )
        for v, k in stats
    ]]
    story.append(Table(stat_rows, colWidths=[22*mm]*8,
        style=TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ])
    ))
    story.append(Spacer(1, 8*mm))

    # ── SECTIONS ──
    col_w = [10*mm, 86*mm, 16*mm, 18*mm]

    for grp in SECTIONS:
        # Group label
        story.append(Paragraph(f"{'🗂️' if 'WORKSPACE' in grp['group'] else '🧠'}  {grp['group']}", S["section_label"]))
        story.append(Paragraph(grp["path"], ParagraphStyle("p", fontName="Courier", fontSize=7, textColor=MUTED, spaceAfter=4)))

        for (section_title, section_color, rows) in grp["items"]:
            # Section header
            story.append(KeepTogether([
                Table(
                    [[Paragraph(section_title, ParagraphStyle("sh2", fontName="Helvetica-Bold",
                                fontSize=9.5, textColor=section_color)),
                      Paragraph(f"{len(rows)} files", ParagraphStyle("sc", fontName="Helvetica",
                                fontSize=7.5, textColor=MUTED, alignment=TA_RIGHT))]],
                    colWidths=[130*mm, 30*mm],
                    style=TableStyle([
                        ("BACKGROUND", (0,0), (-1,-1), SURFACE),
                        ("LINEBELOW", (0,0), (-1,-1), 1.5, section_color),
                        ("TOPPADDING", (0,0), (-1,-1), 5),
                        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
                        ("LEFTPADDING", (0,0), (0,-1), 8),
                    ])
                ),
                Spacer(1, 1),
            ]))

            # Table header
            hdr = [
                Paragraph("#",    ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=7, textColor=MUTED)),
                Paragraph("File", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=7, textColor=MUTED)),
                Paragraph("Fmt",  ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=7, textColor=MUTED, alignment=TA_CENTER)),
                Paragraph("Size", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=7, textColor=MUTED, alignment=TA_RIGHT)),
            ]
            table_data = [hdr]
            table_styles = [
                ("BACKGROUND", (0,0), (-1,0), SURFACE),
                ("LINEBELOW",  (0,0), (-1,0), 0.5, BORDER),
                ("ROWBACKGROUNDS", (0,1), (-1,-1), [ROW_EVEN, ROW_ODD]),
                ("LINEBELOW",  (0,1), (-1,-1), 0.3, BORDER),
                ("ALIGN",      (0,0), (0,-1), "CENTER"),
                ("ALIGN",      (2,0), (2,-1), "CENTER"),
                ("ALIGN",      (3,0), (3,-1), "RIGHT"),
                ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
                ("TOPPADDING",    (0,0), (-1,-1), 4),
                ("BOTTOMPADDING", (0,0), (-1,-1), 4),
                ("LEFTPADDING", (1,0), (1,-1), 4),
            ]
            for num, name, fmt, size in rows:
                fc = FMT_COLORS.get(fmt, MUTED)
                table_data.append([
                    Paragraph(str(num), ParagraphStyle("n", fontName="Helvetica", fontSize=7.5, textColor=MUTED, alignment=TA_CENTER)),
                    Paragraph(name,     ParagraphStyle("nm", fontName="Courier",  fontSize=7.5, textColor=TEXT, leading=11)),
                    Paragraph(fmt,      ParagraphStyle("f",  fontName="Courier-Bold", fontSize=7, textColor=fc, alignment=TA_CENTER, leading=10)),
                    Paragraph(size,     ParagraphStyle("s",  fontName="Helvetica", fontSize=7.5, textColor=MUTED, alignment=TA_RIGHT)),
                ])

            story.append(Table(
                table_data, colWidths=col_w,
                style=TableStyle(table_styles),
                repeatRows=1,
            ))
            story.append(Spacer(1, 5*mm))

    # ── FORMAT SUMMARY ──
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceBefore=6, spaceAfter=6))
    story.append(Paragraph("FORMAT SUMMARY", S["section_label"]))
    fmt_summary = [
        (".md", "37", BLUE), (".png", "44", GREEN), (".pdf", "8", ORANGE),
        (".html", "6", RED), (".webp", "6", ACCENT2), (".mp4", "5", PINK),
        (".jpeg", "2", GREEN), (".docx", "1", CYAN), (".py", "2", colors.HexColor("#a3e635")),
        ("Total", "111", ACCENT2),
    ]
    fmt_table_data = [[
        Table(
            [[Paragraph(v, ParagraphStyle("fv", fontName="Helvetica-Bold", fontSize=13, textColor=fc, alignment=TA_CENTER))],
             [Paragraph(k, ParagraphStyle("fk", fontName="Courier-Bold",   fontSize=7.5, textColor=MUTED, alignment=TA_CENTER))]],
            colWidths=[16*mm],
            style=TableStyle([
                ("BACKGROUND", (0,0), (-1,-1), CARD),
                ("BOX",        (0,0), (-1,-1), 0.5, BORDER),
                ("ALIGN",      (0,0), (-1,-1), "CENTER"),
                ("TOPPADDING",    (0,0), (-1,-1), 4),
                ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ])
        )
        for k, v, fc in fmt_summary
    ]]
    story.append(Table(fmt_table_data, colWidths=[17*mm]*10,
        style=TableStyle([("ALIGN", (0,0), (-1,-1), "CENTER"), ("VALIGN", (0,0), (-1,-1), "MIDDLE")])
    ))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph(
        "Generated by Antigravity  ·  VELYON Legal Command Center  ·  10 April 2026  ·  Attorney-Client Privileged",
        S["footer"]
    ))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF saved: {OUTPUT}")

if __name__ == "__main__":
    build_pdf()
