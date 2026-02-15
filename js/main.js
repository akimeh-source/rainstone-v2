/* ============================================================
   RAINSTONE COMMERCIAL — Main JavaScript
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
    // ---- Mobile Navigation ----
    const toggle = document.getElementById('mobile-toggle');
    const nav = document.getElementById('main-nav');
    let overlay = document.createElement('div');
    overlay.className = 'nav-overlay';
    document.body.appendChild(overlay);

    function openNav() {
        nav.classList.add('open');
        toggle.classList.add('active');
        toggle.setAttribute('aria-expanded', 'true');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeNav() {
        nav.classList.remove('open');
        toggle.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    toggle.addEventListener('click', () => {
        nav.classList.contains('open') ? closeNav() : openNav();
    });

    overlay.addEventListener('click', closeNav);

    // Mobile dropdown toggles
    document.querySelectorAll('.has-dropdown > a').forEach(link => {
        link.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                const parent = link.parentElement;
                parent.classList.toggle('open');
            }
        });
    });

    // Close mobile nav on anchor click
    document.querySelectorAll('.nav-list a[href^="#"]').forEach(a => {
        a.addEventListener('click', () => {
            if (window.innerWidth <= 768) closeNav();
        });
    });

    // ---- Sticky Header Shadow ----
    const header = document.getElementById('site-header');
    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 10);
    }, { passive: true });

    // ---- Smooth Scroll for Anchor Links ----
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerH = header.offsetHeight;
                const top = target.getBoundingClientRect().top + window.scrollY - headerH - 20;
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });

    // ---- FAQ Accordion ----
    document.querySelectorAll('.faq-question').forEach(btn => {
        btn.addEventListener('click', () => {
            const item = btn.parentElement;
            const isActive = item.classList.contains('active');

            // Close all
            document.querySelectorAll('.faq-item').forEach(i => {
                i.classList.remove('active');
                i.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
            });

            // Open clicked (if it was closed)
            if (!isActive) {
                item.classList.add('active');
                btn.setAttribute('aria-expanded', 'true');
            }
        });
    });

    // ---- Back to Top ----
    const btt = document.getElementById('back-to-top');
    window.addEventListener('scroll', () => {
        btt.classList.toggle('visible', window.scrollY > 600);
    }, { passive: true });
    btt.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // ---- Scroll Animations (Intersection Observer) ----
    const animatedEls = document.querySelectorAll('[data-animate]');
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const delay = entry.target.dataset.delay || 0;
                    setTimeout(() => {
                        entry.target.classList.add('animated');
                    }, Number(delay));
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

        animatedEls.forEach(el => observer.observe(el));
    } else {
        // Fallback: show everything
        animatedEls.forEach(el => el.classList.add('animated'));
    }

    // ---- Contact Form (basic validation + UX) ----
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = form.querySelector('#first-name');
            const email = form.querySelector('#email');
            let valid = true;

            // Simple validation
            [name, email].forEach(field => {
                field.style.borderColor = '';
                if (!field.value.trim()) {
                    field.style.borderColor = '#c0392b';
                    valid = false;
                }
            });

            if (email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
                email.style.borderColor = '#c0392b';
                valid = false;
            }

            if (valid) {
                const btn = form.querySelector('button[type="submit"]');
                const originalText = btn.innerHTML;
                btn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
                btn.style.background = '#2A5A3F';
                btn.disabled = true;

                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.style.background = '';
                    btn.disabled = false;
                    form.reset();
                }, 3000);
            }
        });
    }

    // ---- Stat Counter Animation ----
    const statNumbers = document.querySelectorAll('.stat-number');
    if (statNumbers.length && 'IntersectionObserver' in window) {
        const statObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const finalText = el.textContent;
                    const finalVal = parseFloat(finalText);
                    if (isNaN(finalVal)) return;

                    let current = 0;
                    const step = finalVal / 40;
                    const suffix = finalText.replace(/[\d.]/g, '');

                    const timer = setInterval(() => {
                        current += step;
                        if (current >= finalVal) {
                            current = finalVal;
                            clearInterval(timer);
                        }
                        el.textContent = current.toFixed(1) + suffix;
                    }, 30);

                    statObserver.unobserve(el);
                }
            });
        }, { threshold: 0.5 });

        statNumbers.forEach(el => statObserver.observe(el));
    }
});
