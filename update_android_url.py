
import os

root_dir = "/Users/takekei0913/Develop/gitHubPagesForAppInfo/PrivacyPolicies_TermsAndConditions/NumberPlaceHint"
langs = ['de', 'en', 'es', 'fr', 'hi', 'id', 'it', 'ja', 'ko', 'pt', 'ru', 'zh_CN', 'zh_TW']
android_url = "https://play.google.com/store/apps/details?id=com.NumberPlaceHint.takekapp1990.prod"

for lang in langs:
    file_path = os.path.join(root_dir, lang, f"landing_page_{lang}.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace the placeholder # for the android badge link
        # Detailed regex or finding unique context might be safer, 
        # but since we know the context is likely <a href="#" class="store-badge">...badgeAndroid...
        # Let's try to be specific.
        
        # We look for the anchor tag surrounding the Android badge image
        # Because we don't have a unique ID for the Android link in the new code yet (some files might not),
        # but the image src is unique: badgeAndroid
        
        # Strategy: detailed replacement
        # Find: <a href="#" class="store-badge">\n\s*<img src="...badgeAndroid...
        # Replace href="#" with href="URL"
        
        # Simpler approach: replace all href="#" that are followed strictly by android badge logic? 
        # Actually, let's just look for the block.
        
        # Using a more robust replace logic if possible, or just exact string match if formatting is consistent.
        # Since I generated the file content or it is consistent, I can likely match the block.
        
        # However, to be safe and avoiding regex complexity in python for this, 
        # let's assume the previous `grep` showed consistent `href="#" class="store-badge"`.
        # And we distinguish Android vs iOS by the image inside.
        
        # Let's read line by line or use a marker.
        
        lines = content.split('\n')
        new_lines = []
        is_android_link = False
        
        for i, line in enumerate(lines):
            # Check if this line is an anchor with #
            if 'href="#"' in line and 'class="store-badge"' in line:
                # Look ahead to see if it's android
                # Context is small, maybe next line or next next line has badgeAndroid
                found_android = False
                for j in range(1, 4):
                    if i + j < len(lines) and "badgeAndroid" in lines[i+j]:
                        found_android = True
                        break
                
                if found_android:
                    line = line.replace('href="#"', f'href="{android_url}"')
            
            new_lines.append(line)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('\n'.join(new_lines))
            
        print(f"Updated {lang}")

print("Done.")
