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

    // Auto-select current language in switcher
    const langSwitcher = document.getElementById('langSwitcher');
    if (langSwitcher) {
        const currentPath = window.location.pathname;
        for (let option of langSwitcher.options) {
            const pathEnd = option.value.replace('../', '');
            if (currentPath.includes(pathEnd)) {
                option.selected = true;
                break;
            }
        }
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

    // Hero Carousel Animation - starts when visible in viewport
    const carouselContainer = document.getElementById('heroCarousel');
    if (carouselContainer) {
        const images = carouselContainer.querySelectorAll('img');
        let currentIndex = 0;
        let carouselInterval = null;

        const startCarousel = () => {
            if (carouselInterval || images.length <= 1) return;
            carouselInterval = setInterval(() => {
                images[currentIndex].classList.remove('active');
                currentIndex = (currentIndex + 1) % images.length;
                images[currentIndex].classList.add('active');
            }, 2000);
        };

        const stopCarousel = () => {
            if (carouselInterval) {
                clearInterval(carouselInterval);
                carouselInterval = null;
            }
        };

        const carouselObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    startCarousel();
                } else {
                    stopCarousel();
                }
            });
        }, { threshold: 0.3 });

        carouselObserver.observe(carouselContainer);
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
        let currentFeatureIndex = 0;
        let isUserInteracting = false;
        let interactionTimeout;

        const updateDots = (index) => {
            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === index);
            });
        };

        const autoScrollFeatures = () => {
            if (isUserInteracting || window.innerWidth > 900) return;
            
            currentFeatureIndex = (currentFeatureIndex + 1) % featureCards.length;
            const targetCard = featureCards[currentFeatureIndex];
            
            featureWrapper.scrollTo({
                left: targetCard.offsetLeft - (featureWrapper.offsetWidth - targetCard.offsetWidth) / 2,
                behavior: 'smooth'
            });
            updateDots(currentFeatureIndex);
        };

        // Auto-scroll every 4 seconds
        let scrollInterval = setInterval(autoScrollFeatures, 4000);

        // Restart/Reset the auto-scroll timer
        const resetAutoScrollTimer = () => {
            clearInterval(scrollInterval);
            scrollInterval = setInterval(autoScrollFeatures, 4000);
        };

        // Pause auto-scroll on interaction
        featureWrapper.addEventListener('touchstart', () => {
            isUserInteracting = true;
            clearTimeout(interactionTimeout);
        }, {passive: true});

        const handleInteractionEnd = () => {
            clearTimeout(interactionTimeout);
            interactionTimeout = setTimeout(() => {
                isUserInteracting = false;
                resetAutoScrollTimer(); // Restart the interval cycle
            }, 6000); // Resume after 6s of inactivity
        };

        featureWrapper.addEventListener('touchend', handleInteractionEnd, {passive: true});
        featureWrapper.addEventListener('scroll', () => {
            // If the user is scrolling manually, mark as interacting
            if (!isUserInteracting) {
                isUserInteracting = true;
                handleInteractionEnd();
            }

            const wrapperRect = featureWrapper.getBoundingClientRect();
            const wrapperCenter = wrapperRect.left + wrapperRect.width / 2;

            let minDistance = Infinity;
            let detectedIndex = 0;

            featureCards.forEach((card, index) => {
                const cardRect = card.getBoundingClientRect();
                const cardCenter = cardRect.left + cardRect.width / 2;
                const distance = Math.abs(wrapperCenter - cardCenter);

                if (distance < minDistance) {
                    minDistance = distance;
                    detectedIndex = index;
                }
            });

            currentFeatureIndex = detectedIndex;
            updateDots(currentFeatureIndex);
        });
    }
});
