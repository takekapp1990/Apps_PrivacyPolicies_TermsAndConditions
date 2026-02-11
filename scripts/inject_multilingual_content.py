
import os

def inject_content():
    index_path = 'index.html'
    content_path = 'temp_multilingual_content.html'
    
    with open(index_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    with open(content_path, 'r', encoding='utf-8') as f:
        new_content = f.read()
        
    # Find insertion point: Before <!-- Webツールセクション --> and inside #apps section
    # Actually, look for id="apps-en" closing div, or just look for <!-- Webツールセクション --> and go back a few lines to find </section>
    
    insertion_index = -1
    for i, line in enumerate(lines):
        if '<!-- Webツールセクション -->' in line:
            # We want to insert BEFORE the previous </section> line, which closes #apps
            # Let's find </section> backwards from here
            for j in range(i, 0, -1):
                if '</section>' in lines[j]:
                    insertion_index = j
                    break
            break
            
    if insertion_index != -1:
        # Insert before </section>
        # Add a newline before insertion for cleanliness
        lines.insert(insertion_index, new_content + '\n')
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print("Successfully injected content into index.html")
    else:
        print("Could not find insertion point")

if __name__ == "__main__":
    inject_content()
