
import datetime
import re
from pathlib import Path

def generate_sitemap():
    js_file_path = 'js/apps_data.js'
    sitemap_path = 'sitemap.xml'
    base_url = 'https://takekapp.com'
    
    urls = set()
    
    # 1. Add key static pages
    urls.add(f'{base_url}/index.html')
    urls.add(f'{base_url}/')
    
    # 2. Collect all public HTML pages from repository
    for html_path in Path('.').rglob('*.html'):
        parts = html_path.parts
        if any(part.startswith('.') for part in parts):
            continue
        rel_path = html_path.as_posix().lstrip('./')
        urls.add(f'{base_url}/{rel_path}')

    # 3. Extract URLs from apps_data.js (kept as safety net for LP links)
    try:
        with open(js_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = re.findall(r"lp:\s*['\"](https://takekapp\.com/[^'\"]+)['\"]", content)
            for url in matches:
                urls.add(url)
                
    except FileNotFoundError:
        print(f"Error: {js_file_path} not found.")
        # Continue with file system URLs only

    # 4. Generate XML
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    # Current date for lastmod
    today = datetime.date.today().isoformat()
    
    for url in sorted(urls):
        xml_content.append('  <url>')
        xml_content.append(f'    <loc>{url}</loc>')
        xml_content.append(f'    <lastmod>{today}</lastmod>')
        # Priority logic: top pages 1.0, others 0.8
        if url.endswith('index.html') or url == f'{base_url}/':
             xml_content.append('    <priority>1.0</priority>')
        else:
             xml_content.append('    <priority>0.8</priority>')
        xml_content.append('  </url>')
        
    xml_content.append('</urlset>')
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_content))
    
    print(f"Successfully generated {sitemap_path} with {len(urls)} URLs.")

if __name__ == "__main__":
    generate_sitemap()
