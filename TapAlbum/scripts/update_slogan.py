import os
import re

translations = {
    'ja': {
        'slogan': '画面タップで楽しいエフェクト。',
        'feature_title': '楽しいエフェクト',
        'magic_pattern': r'触れるたびに(?:<br class="mobile-only">)?魔法がかかる。?'
    },
    'en': {
        'slogan': 'Fun effects with screen taps.',
        'feature_title': 'Fun Effects',
        'magic_pattern': r'Magic (?:happens with every|at every) touch\.?'
    },
    'es': {
        'slogan': 'Divertidos efectos al tocar la pantalla.',
        'feature_title': 'Efectos Divertidos',
        'magic_pattern': r'La magia ocurre con cada toque\.?'
    },
    'pt': {
        'slogan': 'Efeitos divertidos ao tocar no ecrã.',
        'feature_title': 'Efeitos Divertidos',
        'magic_pattern': r'A magia acontece a cada toque\.?'
    },
    'fr': {
        'slogan': "Des effets amusants en touchant l'écran.",
        'feature_title': 'Effets Amusants',
        'magic_pattern': r'La magie opère à chaque (?:touche?|contact)\.?'
    },
    'de': {
        'slogan': 'Lustige Effekte beim Tippen auf den Bildschirm.',
        'feature_title': 'Lustige Effekte',
        'magic_pattern': r'Magie bei jeder Berührung\.?'
    },
    'it': {
        'slogan': 'Effetti divertenti toccando lo schermo.',
        'feature_title': 'Effetti Divertenti',
        'magic_pattern': r'La magia accade (?:ad ogni|con ogni) tocco\.?'
    },
    'ko': {
        'slogan': '화면을 탭하면 즐거운 효과.',
        'feature_title': '즐거운 효과',
        'magic_pattern': r'터치할 때마다 마법이 (?:걸리는|일어납니다)\.?'
    },
    'zh_Hans': {
        'slogan': '点击屏幕即可享受有趣效果。',
        'feature_title': '有趣特效',
        'magic_pattern': r'每[一]?次触碰都有魔法。?'
    },
    'zh_Hant': {
        'slogan': '點擊屏幕即可享受有趣效果。',
        'feature_title': '有趣特效',
        'magic_pattern': r'每[一]?次觸碰都有魔法。?'
    },
    'ru': {
        'slogan': 'Веселые эффекты при касании экрана.',
        'feature_title': 'Веселые эффекты',
        'magic_pattern': r'Магия (?:в каждом касании|при каждом прикосновении)\.?'
    },
    'ar': {
        'slogan': 'تأثيرات ممتعة مع نقرات الشاشة.',
        'feature_title': 'تأثيرات ممتعة',
        'magic_pattern': r'(?:سحر|يحدث السحر) مع كل لمسة\.?'
    },
    'hi': {
        'slogan': 'स्क्रीन टैप के साथ मजेदार प्रभाव।',
        'feature_title': 'मजेदार प्रभाव',
        'magic_pattern': r'हर स्पर्श (?:पर|के साथ) जादू होता है।?'
    },
    'bn': {
        'slogan': 'স্ক্রিন ট্যাপের সাথে মজার এফেক্ট।',
        'feature_title': 'মজার এফেক্ট',
        'magic_pattern': r'প্রতিটি স্পর্শে জাদু ঘটে।?'
    },
    'id': {
        'slogan': 'Efek menyenangkan dengan ketukan layar.',
        'feature_title': 'Efek Menyenangkan',
        'magic_pattern': r'Keajaiban (?:di setiap|terjadi di setiap) sentuhan\.?'
    },
    'tr': {
        'slogan': 'Ekran dokunuşlarıyla eğlenceli efektler.',
        'feature_title': 'Eğlenceli Efektler',
        'magic_pattern': r'Her dokunuşta sihir (?:gerçekleşir|var)\.?'
    },
    'th': {
        'slogan': 'เอฟเฟกต์สนุกๆ เมื่อแตะหน้าจอ',
        'feature_title': 'เอฟเฟกต์สนุกๆ',
        'magic_pattern': r'(?:ความมหัศจรรย์เกิดขึ้นได้ในทุกสัมผัส|ความมหัศจรรย์เกิดขึ้นได้ในทุกสัมผัส)\.?'
    },
    'vi': {
        'slogan': 'Hiệu ứng vui nhộn khi chạm màn hình.',
        'feature_title': 'Hiệu ứng vui nhộn',
        'magic_pattern': r'Phép (?:thuật|màu) (?:trong mỗi lần chạm|xảy ra sau mỗi lần chạm)\.?'
    },
    'nl': {
        'slogan': 'Leuke effecten bij het tikken op het scherm.',
        'feature_title': 'Leuke effecten',
        'magic_pattern': r'Magie (?:bij elke aanraking|gebeurt bij elke aanraking)\.?'
    },
    'pl': {
        'slogan': 'Zabawne efekty przy dotknięciu ekranu.',
        'feature_title': 'Zabawne efekty',
        'magic_pattern': r'Magia dzieje się przy każdym dotyku\.?'
    },
    'uk': {
        'slogan': 'Веселі ефекти при торканні екрана.',
        'feature_title': 'Веселі ефекти',
        'magic_pattern': r'Магія (?:в кожному дотику|стається при кожному дотику)\.?'
    },
    'da': {
        'slogan': 'Sjove effekter med tryk på skærmen.',
        'feature_title': 'Sjove effekter',
        'magic_pattern': r'Magi sker ved hver berøring\.?'
    },
    'no': {
        'slogan': 'Morsomme effekter med trykk på skjermen.',
        'feature_title': 'Morsomme effekter',
        'magic_pattern': r'Magi skjer ved hver berøring\.?'
    },
    'sw': {
        'slogan': 'Athari za kufurahisha kwa kugonga skrini.',
        'feature_title': 'Athari za kufurahisha',
        'magic_pattern': r'Uchawi hutokea kwa kila mguso\.?'
    }
}

feature_magic_patterns = {
    'ja': '魔法のエフェクト',
    'en': 'Magical Effects',
    'es': 'Efectos Mágicos',
    'pt': 'Efeitos Mágicos',
    'fr': 'Effets Magiques',
    'de': 'Magische Effekte',
    'it': 'Effetti magici',
    'ko': '마법의 효과',
    'zh_Hans': '魔法特效',
    'zh_Hant': '魔法特效',
    'ru': 'Магические эффекты',
    'ar': 'تأثيرات سحرية',
    'hi': 'जादुई प्रभाव',
    'bn': 'জাদুকরী প্রভাব',
    'id': 'Efek Ajaib',
    'tr': 'Sihirli Efektler',
    'th': 'เอฟเฟกต์มหัศจรรย์',
    'vi': 'Hiệu ứng kỳ ảo',
    'nl': 'Magische effecten',
    'pl': 'Magiczne efekty',
    'uk': 'Магічні ефекти',
    'da': 'Magiske effekter',
    'no': 'Magiske effekter',
    'sw': 'Athari za Kichawi'
}

base_dir = '.' # Should be run from TapAlbum/scripts/.. or adjusted

for lang, data in translations.items():
    file_path = os.path.join('TapAlbum', lang, f'landing_page_{lang}.html')
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace localized slogan
    # We use a looser regex to match variations and potential line breaks (though regex doesn't match cross-line by default)
    # But let's try to match exactly what we saw in grep.
    
    # Handle the H1 case specifically for JA
    if lang == 'ja':
        content = content.replace('触れるたびに<br class="mobile-only">魔法がかかる。', '画面タップで<br class="mobile-only">楽しいエフェクト。')
    
    content = re.sub(data['magic_pattern'], data['slogan'], content)

    # 2. Replace literal English slogan (often used as placeholder in OGP)
    # Magic happens with every touch.
    content = re.sub(r'Magic happens with every touch\.?', data['slogan'], content)
    # Magic at every touch
    content = re.sub(r'Magic at every touch\.?', data['slogan'], content)

    # 3. Replace Feature Title
    if lang in feature_magic_patterns:
        content = content.replace(feature_magic_patterns[lang], data['feature_title'])
    
    # Fallback for English feature title if not replaced
    content = content.replace('Magical Effects', data['feature_title'])

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {file_path}")
