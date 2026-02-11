
function renderApps(lang) {
    // In hybrid approach, JA and EN are static. If we accidentally call this for them, do nothing or return.
    if (lang === 'ja' || lang === 'en') return;

    const container = document.getElementById('dynamic-app-container');
    if (!container) return;

    container.innerHTML = ''; // Clear existing content
    
    // Add section title for consistency
    const title = document.createElement('h2');
    title.className = 'section-title';
    title.textContent = 'Apps'; // localized? maybe 'Apps' is fine for now, or map it.
    container.appendChild(title);
    
    const row = document.createElement('div');
    row.className = 'row';
    container.appendChild(row);

    // Determine fallback language order
    const langFallbacks = [lang, 'en', 'ja'];

    appsData.forEach(app => {
        // Find best matching locale data
        let appLocale = null;
        let usedLang = null;

        for (const l of langFallbacks) {
            if (app.locales[l]) {
                appLocale = app.locales[l];
                usedLang = l;
                break;
            }
        }

        // If no locale data found (e.g. app only in Japanese and user selected German, and we didn't add English fallback in data), skip or show Japanese?
        // Current logic: we check requested lang, then EN, then JA.
        // If the app supports the requested language, we show it.
        // BUT strict requirement: "FlagMemoryAwaAwaPon: de, es, id, ko, th"
        // If we switch to 'de', we should show FlagMemory with DE data.
        // If we switch to 'de', should we show "Good Luck Maker" which only has JA/EN?
        // Use case: Adding multilingual support implies showing apps RELEVANT to that language or GLOBAL apps.
        // IF we want to show ALL apps, falling back to English: valid.
        // IF we want to show ONLY apps that support that language: strictly filter.
        
        // Let's assume we show apps that have data for the requested language OR are generally available (falling back to English).
        // However, the user specifically mentioned "Identified Supported Languages" for specific apps.
        // This implies for 'de', primarily those apps should be highlighted, or maybe only those?
        // Let's stick to: Show app if it has content for 'lang'.
        // If we want to show everything, we use fallback.
        // Given the goal is "Add Multilingual Support", if I visit 'es' and see 'Good Luck Maker' in English, is that good?
        // Probably yes, it's better than empty space.
        // But for this task, I will prioritize showing the localized content.
        
        // Let's rely on the existence of `app.locales[lang]` to decide if it's "officially supported" in that language.
        // If not, maybe we skip it to keep the list relevant?
        // User said: "Create new content sections... displaying relevant apps".
        // So I should probably filter by `app.locales[lang]`.
        
        // HOWEVER, for JA and EN, we show everything (as they are base languages).
        // Let's implement Filter Strictness:
        // If lang is JA or EN, show everything (fallback to EN/JA if needed).
        // If lang is others, ONLY show apps that have that specific locale defined.
        
        if (lang !== 'ja' && lang !== 'en' && !app.locales[lang]) {
            return; // Skip this app for this language
        }
        
        // If we are JA/EN, or we found the locale, we proceed.
        // If JA/EN and missing specific locale, fallback.
        if (!appLocale) {
             // Fallback for JA/EN if missing
             for (const l of ['en', 'ja']) {
                if (app.locales[l]) {
                    appLocale = app.locales[l];
                    break;
                }
            }
        }

        if (!appLocale) return; // Should not happen given data

        const col = document.createElement('div');
        col.className = 'col-lg-6 col-xl-4 mb-4';

        // Terms/Privacy buttons only for JA/EN
        let policyButtons = '';
        if (lang === 'ja' || lang === 'en') {
            policyButtons = `
                <div class="policy-buttons">
                    <a href="https://takekapp.com/${app.id}/${lang === 'ja' ? 'ja' : 'en'}/terms_and_conditions_${lang === 'ja' ? 'ja' : 'en'}.html"
                        class="btn btn-outline-primary">${lang === 'ja' ? '利用規約' : 'Terms and Conditions'}</a>
                    <a href="https://takekapp.com/${app.id}/${lang === 'ja' ? 'ja' : 'en'}/privacy_policy_${lang === 'ja' ? 'ja' : 'en'}.html"
                        class="btn btn-outline-primary">${lang === 'ja' ? 'プライバシーポリシー' : 'Privacy Policy'}</a>
                </div>
            `;
        }
        
        // Correct landing page URL is in the locale data
        const lpUrl = appLocale.lp;
        
        // Description fallback: if null, try EN, then JA
        let description = appLocale.description;
        if (!description) {
            if (app.locales['en'] && app.locales['en'].description) {
                description = app.locales['en'].description;
            } else if (app.locales['ja'] && app.locales['ja'].description) {
                description = app.locales['ja'].description;
            }
        }
        let androidBadge = '';
        if (app.android) {
            androidBadge = `
                <a href="${app.android}" target="_blank" class="app-store-badge">
                    <img src="https://takekapp.com/commonImages/badgeAndroid/GetItOnGooglePlay_Badge_Web_color_${lang === 'ja' ? 'Japanese' : 'English'}.png"
                        alt="${lang === 'ja' ? 'Google Playで手に入れよう' : 'Get it on Google Play'}" height="40">
                </a>
            `;
        }
        
        let iosBadge = '';
        if (app.ios) {
             iosBadge = `
                <a href="${app.ios}" target="_blank" class="app-store-badge">
                    <img src="https://takekapp.com/commonImages/badgeiOSAppStore/Download_on_the_App_Store_Badge_${lang === 'ja' ? 'JP_RGB_blk_100317' : 'US-UK_RGB_blk_092917'}.svg"
                        alt="${lang === 'ja' ? 'App Storeからダウンロード' : 'Download on the App Store'}" height="40">
                </a>
            `;
        }

        col.innerHTML = `
            <div class="card app-card h-100">
                <div class="card-body">
                    <div class="d-flex mb-3">
                        <img src="${app.icon}" class="app-icon me-3" alt="${appLocale.title}">
                        <div>
                            <h3 class="card-title">
                                <a href="${lpUrl}" class="text-decoration-none text-primary">${appLocale.title}</a>
                            </h3>
                            <p class="card-text">${description}</p>
                        </div>
                    </div>
                    <div class="d-flex flex-column gap-2">
                        <a href="${lpUrl}" class="btn btn-primary">${lang === 'ja' ? '詳細を見る' : 'Learn More'}</a>
                        <div class="d-flex gap-2 justify-content-center">
                            ${androidBadge}
                            ${iosBadge}
                        </div>
                        ${policyButtons}
                    </div>
                </div>
            </div>
        `;

        row.appendChild(col);
    });
}
