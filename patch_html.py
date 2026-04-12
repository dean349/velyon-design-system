import os
import datetime
from bs4 import BeautifulSoup
from urllib.parse import unquote

HTML_FILE = 'd:\\VELYON - LEGAL COMMAND CENTER\\Antigravity_Files_Produced_Last_48hrs.html'
WORKSPACE = 'd:\\VELYON - LEGAL COMMAND CENTER\\'

LINKS_TO_ADD = [
    "https://velyon.io/",
    "https://dean349.github.io/LosRomeros-BrandCommandCentral/",
    "https://dean349.github.io/Wincham-claim-overview-HARRISON-EXPERT-ADVISORS/",
    "https://dean349.github.io/antigravity-capabilities/",
    "https://dean349.github.io/phil-harrison-forensic-report/",
    "https://dean349.github.io/wincham-scheme-illegal/",
    "https://dean349.github.io/lanzarote-forensic-portal/executive_briefing.html",
    "https://dean349.github.io/philip-harrison-negligent-claims-against-wincham/",
    "https://dean349.github.io/philip-harrison-emergency-bank-plan/",
    "https://dean349.github.io/philip-harrison-tide-setup/",
    "https://dean349.github.io/philip-harrison-scenario-planning/",
    "https://dean349.github.io/lanzarote-keep-or-buy/",
    "https://dean349.github.io/Lanzarote-villa-ownership-comparison/",
    "https://dean349.github.io/philip-harrison-lanzarote-spanish-cgt-report/",
    "https://dean349.github.io/philip-harrison-mvl-report/",
    "https://dean349.github.io/wincham-negligence-strategy/",
    "https://dean349.github.io/wincham-giambrone-precedent/",
    "https://dean349.github.io/wincham-glo-opportunity/#strategy",
    "https://dean349.github.io/wincham-lead-generation/",
    "https://dean349.github.io/velyon-design-system/",
    "https://dean349.github.io/ultimate-prompt-landing/",
    "https://github.com/dean349/antigravity-local-skills/settings",
    "https://github.com/dean349/antigravity-global-skills/settings"
]

print("Loading HTML (this may take a moment for large files)...")
with open(HTML_FILE, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

print("Patching tables...")
for table in soup.find_all('table'):
    # Check if this is a file table (headers usually th)
    thead = table.find('thead')
    if not thead:
        # Some tables might just use tr > th
        ths = table.find_all('th')
        if not ths or 'File' not in [th.text.strip() for th in ths]:
            continue
    
    # 1. Update the headers
    header_row = thead.find('tr') if thead else table.find('tr')
    if not header_row: continue
    
    # Only patch if not already patched
    headers = [th.text.strip() for th in header_row.find_all('th')]
    if 'Date Updated' in headers:
        continue
        
    date_th = soup.new_tag('th')
    date_th.string = "Date Updated"
    path_th = soup.new_tag('th')
    path_th.string = "File Path"
    
    # Insert before the last column ('Link' usually) or at the end
    header_row.append(date_th)
    header_row.append(path_th)
    
    # 2. Update all body rows
    tbody = table.find('tbody')
    rows = tbody.find_all('tr') if tbody else table.find_all('tr')[1:]
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) < 2: continue # Safety check
        
        # Try to find the file path via the link if it exists
        links = row.find_all('a')
        rel_path = "Unknown"
        date_str = "Unknown"
        
        if links:
            href = links[0].get('href', '')
            if href.startswith('file:///'):
                # Extract path from absolute file uri
                path_uri = href.replace('file:///', '').replace('file://', '')
                path_uri = unquote(path_uri)
                # Convert backslashes
                path_uri = path_uri.replace('/', '\\')
                
                # Check if it exists
                if os.path.exists(path_uri):
                    mtime = os.path.getmtime(path_uri)
                    dt = datetime.datetime.fromtimestamp(mtime)
                    date_str = dt.strftime("%Y-%m-%d %H:%M")
                    # Try to make it relative
                    if path_uri.lower().startswith(WORKSPACE.lower()):
                        rel_path = path_uri[len(WORKSPACE):].lstrip('\\')
                    else:
                        rel_path = path_uri
                else:
                    rel_path = "File Not Found Locally"
        
        new_td1 = soup.new_tag('td')
        new_td1.string = date_str
        new_td2 = soup.new_tag('td')
        
        # Wrap path in a code tag to make it look nice
        code_tag = soup.new_tag('code', style="font-size: 0.85em; color: #8b95aa; word-break: break-all;")
        code_tag.string = rel_path
        new_td2.append(code_tag)
        
        row.append(new_td1)
        row.append(new_td2)

print("Injecting links section at the top...")
# Find the hero container or main wrapper to inject the links
# Typically there's a <body> tag, or a <main> tag, or a <div class="container">
container = soup.find('div', class_='container')
if not container:
    container = soup.body

if container:
    # Create the block
    links_div = soup.new_tag('div')
    links_div['style'] = "background-color: #1a1e2a; border: 1px solid #252a38; border-radius: 8px; padding: 20px; margin: 30px auto; max-width: 1200px;"
    
    header = soup.new_tag('h2')
    header.string = "🌐 Official Network & Repositories"
    header['style'] = "color: #e2e8f0; margin-top: 0; margin-bottom: 15px; font-size: 1.2em; border-bottom: 1px solid #252a38; padding-bottom: 10px;"
    links_div.append(header)
    
    ul = soup.new_tag('ul')
    ul['style'] = "list-style-type: none; padding-left: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 10px;"
    
    for link in LINKS_TO_ADD:
        li = soup.new_tag('li')
        a = soup.new_tag('a')
        a['href'] = link
        a['target'] = '_blank'
        # Get just the last part of the URL for cleaner display, or use full url
        display_name = link.split('/')[-2] if link.endswith('/') else link.split('/')[-1]
        if not display_name or link == 'https://velyon.io/':
            display_name = link
            
        a.string = "🔗 " + display_name
        a['style'] = "color: #a78bfa; text-decoration: none; font-size: 0.9em; word-break: break-all;"
        
        li.append(a)
        ul.append(li)
        
    links_div.append(ul)
    
    # Try inserting right after the title or header
    title_header = soup.find('h1')
    if title_header and title_header.parent:
        title_header.parent.insert_after(links_div)
    else:
        container.insert(0, links_div)

print("Saving modified HTML...")
with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modification complete!")
