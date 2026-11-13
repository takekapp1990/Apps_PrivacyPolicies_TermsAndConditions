(function () {
    'use strict';

    if (window.__takekCrossAppAnalyticsInitialized) return;
    window.__takekCrossAppAnalyticsInitialized = true;

    document.addEventListener('click', function (event) {
        if (!(event.target instanceof Element)) return;
        const link = event.target.closest('a[data-cross-app]');
        if (!link || typeof window.gtag !== 'function') return;
        // Local previews must not send events to the production property.
        if (!['takekapp.com', 'www.takekapp.com'].includes(window.location.hostname)) return;

        const destination = new URL(link.href, window.location.href);
        if (destination.origin !== window.location.origin) return;

        window.gtag('event', 'cross_app_click', {
            source_app: document.body.dataset.app,
            source_page_type: document.body.dataset.pageType,
            source_path: window.location.pathname,
            destination_app: link.dataset.crossApp,
            link_position: link.dataset.crossAppPosition,
            link_url: destination.href,
            language: document.documentElement.lang,
            transport_type: 'beacon'
        });
    }, { capture: true });
})();
