document.documentElement.classList.add("has-reveal");

window.addEventListener("DOMContentLoaded", () => {
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    const revealTargets = document.querySelectorAll(
        ".feature-stack .screen-card, .product-panel .screen-card",
    );

    if (reduceMotion || !("IntersectionObserver" in window)) {
        revealTargets.forEach((target) => target.classList.add("is-visible"));
    } else {
        revealTargets.forEach((target) => target.classList.add("reveal-pending"));

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                });
            },
            { threshold: 0.12, rootMargin: "0px 0px -8% 0px" },
        );

        revealTargets.forEach((target) => observer.observe(target));
    }

    const languagePickers = document.querySelectorAll(".language-picker");
    document.addEventListener("pointerdown", (event) => {
        languagePickers.forEach((picker) => {
            if (!picker.contains(event.target)) picker.removeAttribute("open");
        });
    });

    languagePickers.forEach((picker) => {
        picker.addEventListener("keydown", (event) => {
            if (event.key !== "Escape") return;
            picker.removeAttribute("open");
            picker.querySelector("summary")?.focus();
        });
    });

    document.querySelectorAll("[data-hero-carousel]").forEach((carousel) => {
        const slides = Array.from(carousel.querySelectorAll("[data-carousel-slide]"));
        const buttons = Array.from(carousel.querySelectorAll("[data-carousel-button]"));
        if (slides.length < 2 || slides.length !== buttons.length) return;

        let currentIndex = Math.max(0, slides.findIndex((slide) => slide.classList.contains("is-active")));
        let timer;

        const showSlide = (nextIndex) => {
            currentIndex = (nextIndex + slides.length) % slides.length;
            slides.forEach((slide, index) => {
                const active = index === currentIndex;
                slide.classList.toggle("is-active", active);
                slide.setAttribute("aria-hidden", String(!active));
            });
            buttons.forEach((button, index) => {
                const active = index === currentIndex;
                button.classList.toggle("is-active", active);
                button.setAttribute("aria-pressed", String(active));
            });
        };

        const stop = () => {
            if (timer) window.clearInterval(timer);
            timer = undefined;
        };

        const start = () => {
            if (
                reduceMotion ||
                timer ||
                document.hidden ||
                carousel.matches(":hover") ||
                carousel.contains(document.activeElement)
            ) return;
            timer = window.setInterval(() => showSlide(currentIndex + 1), 6000);
        };

        buttons.forEach((button, index) => {
            button.addEventListener("click", () => {
                stop();
                showSlide(index);
                start();
            });
        });

        carousel.addEventListener("mouseenter", stop);
        carousel.addEventListener("mouseleave", start);
        carousel.addEventListener("focusin", stop);
        carousel.addEventListener("focusout", (event) => {
            if (!carousel.contains(event.relatedTarget)) start();
        });
        carousel.addEventListener("keydown", (event) => {
            if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
            event.preventDefault();
            stop();
            showSlide(currentIndex + (event.key === "ArrowRight" ? 1 : -1));
            buttons[currentIndex].focus();
        });
        document.addEventListener("visibilitychange", () => {
            if (document.hidden) stop();
            else start();
        });

        showSlide(currentIndex);
        start();
    });
});
