(function () {
    'use strict';

    if (window.__takekAppStoreAnalyticsInitialized) return;
    window.__takekAppStoreAnalyticsInitialized = true;

    const STORE_HOSTS = {
        'apps.apple.com': 'app_store',
        'apple.co': 'app_store',
        'toolbox.marketingtools.apple.com': 'app_store',
        'play.google.com': 'google_play'
    };

    function getSourcePage() {
        const canonical = document.querySelector('link[rel="canonical"]');
        try {
            return new URL(canonical ? canonical.href : window.location.href, window.location.href);
        } catch (error) {
            return new URL(window.location.href);
        }
    }

    function getLinkPosition(link) {
        if (link.dataset.analyticsPosition) return link.dataset.analyticsPosition;

        const section = link.closest('section[id]');
        if (section) return section.id;
        if (link.closest('.hero')) return 'hero';
        if (link.closest('header')) return 'header';
        if (link.closest('footer')) return 'footer';
        return 'content';
    }

    document.addEventListener('click', function (event) {
        if (!(event.target instanceof Element)) return;

        const link = event.target.closest('a[href]');
        if (!link || typeof window.gtag !== 'function') return;

        let destination;
        try {
            destination = new URL(link.href, window.location.href);
        } catch (error) {
            return;
        }

        const storeName = STORE_HOSTS[destination.hostname];
        if (!storeName) return;

        const sourcePage = getSourcePage();
        const pathParts = sourcePage.pathname.split('/').filter(Boolean);

        window.gtag('event', 'app_store_click', {
            store_name: storeName,
            app_name: pathParts[0] || 'takekapp',
            lp_path: sourcePage.pathname,
            link_url: destination.href,
            link_position: getLinkPosition(link)
        });
    }, { capture: true });
})();
