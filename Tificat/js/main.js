// js/main.js

document.addEventListener('DOMContentLoaded', () => {
    // Navbar Scrolled State
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Initialize scrolled state check
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }

    // Intersection Observer for Fade-in-up animation
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                obs.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in-up').forEach((elem) => {
        observer.observe(elem);
    });

    // Hero Carousel Animation (Every 2 seconds)
    const carouselContainer = document.getElementById('heroCarousel');
    if (carouselContainer) {
        const images = carouselContainer.querySelectorAll('img');
        let currentIndex = 0;
        
        if (images.length > 1) {
            setInterval(() => {
                images[currentIndex].classList.remove('active');
                currentIndex = (currentIndex + 1) % images.length;
                images[currentIndex].classList.add('active');
            }, 2000);
        }
    }

    // Feature Carousel Dots Logic for Mobile
    const featureWrapper = document.querySelector('.features-wrapper');
    const featureDots = document.getElementById('featureDots');
    
    if (featureWrapper && featureDots) {
        const featureCards = featureWrapper.querySelectorAll('.feature-row');
        
        featureCards.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.className = 'carousel-dot' + (index === 0 ? ' active' : '');
            featureDots.appendChild(dot);
        });

        const dots = featureDots.querySelectorAll('.carousel-dot');

        featureWrapper.addEventListener('scroll', () => {
            const wrapperRect = featureWrapper.getBoundingClientRect();
            const wrapperCenter = wrapperRect.left + wrapperRect.width / 2;

            let currentIndex = 0;
            let minDistance = Infinity;

            featureCards.forEach((card, index) => {
                const cardRect = card.getBoundingClientRect();
                const cardCenter = cardRect.left + cardRect.width / 2;
                const distance = Math.abs(wrapperCenter - cardCenter);

                if (distance < minDistance) {
                    minDistance = distance;
                    currentIndex = index;
                }
            });

            dots.forEach((dot, index) => {
                if (index === currentIndex) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        });
    }
});
