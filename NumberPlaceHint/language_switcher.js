(function () {
    "use strict";

    const container = document.getElementById("language-switcher");
    if (!container) return;

    if (!document.querySelector('link[href="../language_switcher.css"]')) {
        const stylesheet = document.createElement("link");
        stylesheet.rel = "stylesheet";
        stylesheet.href = "../language_switcher.css";
        document.head.appendChild(stylesheet);
    }

    const languages = [
        ["ja", "日本語", "../ja/landing_page_ja.html"],
        ["en", "English", "../en/landing_page_en.html"],
        ["ar", "العربية", "../ar/landing_page_ar.html"],
        ["da", "Dansk", "../da/landing_page_da.html"],
        ["de", "Deutsch", "../de/landing_page_de.html"],
        ["es", "Español", "../es/landing_page_es.html"],
        ["fr", "Français", "../fr/landing_page_fr.html"],
        ["hi", "हिन्दी", "../hi/landing_page_hi.html"],
        ["id", "Bahasa Indonesia", "../id/landing_page_id.html"],
        ["it", "Italiano", "../it/landing_page_it.html"],
        ["ko", "한국어", "../ko/landing_page_ko.html"],
        ["nl", "Nederlands", "../nl/landing_page_nl.html"],
        ["pl", "Polski", "../pl/landing_page_pl.html"],
        ["pt", "Português", "../pt/landing_page_pt.html"],
        ["ru", "Русский", "../ru/landing_page_ru.html"],
        ["sv", "Svenska", "../sv/landing_page_sv.html"],
        ["th", "ไทย", "../th/landing_page_th.html"],
        ["tr", "Türkçe", "../tr/landing_page_tr.html"],
        ["uk", "Українська", "../uk/landing_page_uk.html"],
        ["vi", "Tiếng Việt", "../vi/landing_page_vi.html"],
        ["zh-CN", "简体中文", "../zh_CN/landing_page_zh_CN.html"],
        ["zh-TW", "繁體中文", "../zh_TW/landing_page_zh_TW.html"]
    ];

    const labels = {
        ar: "اختر اللغة", da: "Vælg sprog", de: "Sprache wählen",
        en: "Choose language", es: "Elegir idioma", fr: "Choisir la langue",
        hi: "भाषा चुनें", id: "Pilih bahasa", it: "Scegli la lingua",
        ja: "言語を選択", ko: "언어 선택", nl: "Taal kiezen", pl: "Wybierz język",
        pt: "Escolher idioma", ru: "Выберите язык", sv: "Välj språk",
        th: "เลือกภาษา", tr: "Dil seçin", uk: "Виберіть мову",
        vi: "Chọn ngôn ngữ", "zh-CN": "选择语言", "zh-TW": "選擇語言"
    };

    const currentLanguage = document.documentElement.lang || "en";
    const labelText = labels[currentLanguage] || labels.en;
    const inner = document.createElement("div");
    inner.className = "language-switcher__inner";

    const label = document.createElement("label");
    label.className = "language-switcher__control";
    label.htmlFor = "language-select";

    const icon = document.createElement("span");
    icon.className = "language-switcher__icon";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = "🌐";

    const hiddenLabel = document.createElement("span");
    hiddenLabel.textContent = labelText;

    const select = document.createElement("select");
    select.id = "language-select";
    select.className = "language-switcher__select";
    select.setAttribute("aria-label", labelText);

    languages.forEach(([code, name, url]) => {
        const option = document.createElement("option");
        option.value = url;
        option.textContent = name;
        option.lang = code;
        option.selected = code === currentLanguage;
        select.appendChild(option);
    });

    select.addEventListener("change", function () {
        window.location.assign(this.value);
    });

    label.append(icon, hiddenLabel, select);
    inner.appendChild(label);
    container.className = "language-switcher";
    container.setAttribute("aria-label", labelText);
    container.appendChild(inner);
})();
