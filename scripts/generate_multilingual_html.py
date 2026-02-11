import os
import re

languages = {
    'es': ['SharedDice', 'FlagMemoryAwaAwaPon', 'TimesTablesMemoryAwaAwaPon', 'NumberPlaceHint'],
    'ko': ['SharedDice', 'FlagMemoryAwaAwaPon', 'TimesTablesMemoryAwaAwaPon', 'NumberPlaceHint'],
    'de': ['SharedDice', 'FlagMemoryAwaAwaPon', 'TimesTablesMemoryAwaAwaPon', 'NumberPlaceHint'],
    'id': ['SharedDice', 'FlagMemoryAwaAwaPon', 'TimesTablesMemoryAwaAwaPon', 'NumberPlaceHint'],
    'th': ['SharedDice', 'FlagMemoryAwaAwaPon', 'TimesTablesMemoryAwaAwaPon'],
    'fr': ['SharedDice', 'NumberPlaceHint'],
    'it': ['SharedDice', 'NumberPlaceHint'],
    'pt': ['SharedDice', 'NumberPlaceHint'],
    'ru': ['SharedDice', 'NumberPlaceHint'],
    'hi': ['SharedDice', 'NumberPlaceHint'],
    'zh_CN': ['SharedDice', 'NumberPlaceHint'],
    'zh_TW': ['SharedDice', 'NumberPlaceHint'],
}

app_info = {
    'SharedDice': {
        'path_pattern': 'SharedDice/landing_pages/{lang}/landing_page_{lang}.html',
        'icon': 'https://takekapp.com/SharedDice/images/icon_512512_app_store.png',
        'android': 'https://play.google.com/store/apps/details?id=com.shared_dice_takekapp.takekapp1990.prod',
        'ios': 'https://apps.apple.com/app/id1583535228',
    },
    'FlagMemoryAwaAwaPon': {
        'path_pattern': 'FlagMemoryAwaAwaPon/{lang}/landing_page_{lang}.html',
        'icon': 'https://takekapp.com/FlagMemoryAwaAwaPon/images/awaawapon_national_flags_app_icon_10241024_ios.png',
        'android': 'https://play.google.com/store/apps/details?id=com.NationalFlagsAwaPop.takekapp1990.prod',
        'ios': 'https://apps.apple.com/us/app/flag-quiz-awa-pop/id6757128485',
    },
    'TimesTablesMemoryAwaAwaPon': {
        'path_pattern': 'TimesTablesMemoryAwaAwaPon/{lang}/landing_page_{lang}.html',
        'icon': 'https://takekapp.com/TimesTablesMemoryAwaAwaPon/images/awaawapon_times_tables_app_icon_10241024_ios.png',
        'android': 'https://play.google.com/store/apps/details?id=com.TimesTablesAwaPop.takekapp1990.prod',
        'ios': 'https://apps.apple.com/us/app/times-tables-memory-awa-pop/id6757520572',
    },
    'NumberPlaceHint': {
        'path_pattern': 'NumberPlaceHint/{lang}/landing_page_{lang}.html',
        'icon': 'https://takekapp.com/NumberPlaceHint/images/app_icon/number_place_hint_app_icon_10241024_ios.png',
        'android': 'https://play.google.com/store/apps/details?id=com.NumberPlaceHint.takekapp1990.prod',
        'ios': 'https://apps.apple.com/jp/app/%E3%83%8A%E3%83%B3%E3%83%97%E3%83%AC%E3%81%AE%E3%83%92%E3%83%B3%E3%83%88/id6758233715',
    }
}

def get_title(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Special logic for FlagMemory ES (use twitter:title)
            if 'FlagMemoryAwaAwaPon' in path and '/es/' in path:
                 match = re.search(r'<meta name="twitter:title" content="([^"]+)"', content)
                 if match: return match.group(1)

            match = re.search(r'<title>([^<]+)</title>', content)
            if match:
                return match.group(1).strip()
    except FileNotFoundError:
        return None
    return None

def generate_html():
    output = ""
    for lang, apps in languages.items():
        output += f'            <div class="content-{lang}" id="apps-{lang}">\n'
        output += f'                <h2 class="section-title">Apps</h2>\n'
        output += f'                <div class="row">\n'
        
        for app_name in apps:
            info = app_info[app_name]
            file_path = info['path_pattern'].format(lang=lang)
            title = get_title(file_path)
            if not title:
                title = app_name # Fallback
            
            lp_url = f"https://takekapp.com/{file_path}"
            
            output += f'                    <div class="col-lg-6 col-xl-4 mb-4">\n'
            output += f'                        <div class="card app-card h-100">\n'
            output += f'                            <div class="card-body">\n'
            output += f'                                <div class="d-flex mb-3">\n'
            output += f'                                    <img src="{info["icon"]}" class="app-icon me-3" alt="{title}">\n'
            output += f'                                    <div>\n'
            output += f'                                        <h3 class="card-title">\n'
            output += f'                                            <a href="{lp_url}" class="text-decoration-none text-primary">{title}</a>\n'
            output += f'                                        </h3>\n'
            output += f'                                        <p class="card-text"></p>\n'
            output += f'                                    </div>\n'
            output += f'                                </div>\n'
            output += f'                                <div class="d-flex flex-column gap-2">\n'
            output += f'                                    <a href="{lp_url}" class="btn btn-primary">Open Page</a>\n'
            output += f'                                    <div class="d-flex gap-2 justify-content-center">\n'
            output += f'                                        <a href="{info["android"]}" target="_blank" class="app-store-badge">\n'
            output += f'                                            <img src="https://takekapp.com/commonImages/badgeAndroid/GetItOnGooglePlay_Badge_Web_color_English.png" alt="Get it on Google Play" height="40">\n'
            output += f'                                        </a>\n'
            output += f'                                        <a href="{info["ios"]}" target="_blank" class="app-store-badge">\n'
            output += f'                                            <img src="https://takekapp.com/commonImages/badgeiOSAppStore/Download_on_the_App_Store_Badge_US-UK_RGB_blk_092917.svg" alt="Download on the App Store" height="40">\n'
            output += f'                                        </a>\n'
            output += f'                                    </div>\n'
            output += f'                                </div>\n'
            output += f'                            </div>\n'
            output += f'                        </div>\n'
            output += f'                    </div>\n'

        output += f'                </div>\n'
        output += f'            </div>\n'
    with open('temp_multilingual_content.html', 'w', encoding='utf-8') as f:
        f.write(output)
    print("HTML written to temp_multilingual_content.html")

if __name__ == "__main__":
    generate_html()
