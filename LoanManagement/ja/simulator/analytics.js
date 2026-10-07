// Track only interaction type on the public site. Never send loan inputs/results.
// Local previews do not load analytics or send events.
(() => {
  if (location.hostname !== 'takekapp.com' && location.hostname !== 'www.takekapp.com') return;
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', 'G-0VCS46ZTHC');
  const script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=G-0VCS46ZTHC';
  document.head.appendChild(script);
})();
