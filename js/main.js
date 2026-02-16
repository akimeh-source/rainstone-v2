/* ============================================================
   RAINSTONE COMMERCIAL — Main JavaScript
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
    // ---- Mode Tab Switching (Personal / Commercial) ----
    const modeTabs = document.querySelectorAll('.mode-tab');
    const logoTagline = document.getElementById('logo-tagline');

    modeTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const mode = tab.dataset.tab;
            document.body.setAttribute('data-mode', mode);

            // Update active tab
            modeTabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Update logo tagline
            if (logoTagline) {
                logoTagline.textContent = mode === 'commercial' ? 'COMMERCIAL' : 'MONEY';
            }

            // Handle commercial video play/pause
            const video = document.querySelector('.hero-video');
            if (video) {
                if (mode === 'commercial') {
                    // Small delay lets the browser paint the now-visible element
                    requestAnimationFrame(() => {
                        video.currentTime = 0;
                        video.play().catch(() => {});
                    });
                } else {
                    video.pause();
                }
            }

            // Re-trigger animations on newly visible sections
            document.querySelectorAll('.tab-' + mode + ' [data-animate]').forEach(el => {
                if (!el.classList.contains('animated')) {
                    el.classList.add('animated');
                }
            });

            // Scroll to top of page on switch
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });

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

    // ---- Sticky Header + Scroll Progress ----
    const header = document.getElementById('site-header');
    const scrollProgress = document.getElementById('scroll-progress');

    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 10);

        // Update scroll progress bar
        if (scrollProgress) {
            const docH = document.documentElement.scrollHeight - window.innerHeight;
            const pct = docH > 0 ? (window.scrollY / docH) * 100 : 0;
            scrollProgress.style.width = pct + '%';
        }
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

    // ---- Mortgage Calculator ----
    const calcBtn = document.getElementById('calc-btn');
    const calcTermSlider = document.getElementById('calc-term');
    const calcTermVal = document.getElementById('calc-term-val');
    const calcDebt = document.getElementById('calc-debt');

    if (calcTermSlider && calcTermVal) {
        calcTermSlider.addEventListener('input', () => {
            calcTermVal.textContent = calcTermSlider.value;
        });
    }

    // Live comma formatting on debt input
    if (calcDebt) {
        calcDebt.addEventListener('input', () => {
            const raw = calcDebt.value.replace(/[^0-9]/g, '');
            if (raw) {
                calcDebt.value = parseInt(raw, 10).toLocaleString('en-GB');
            }
        });
    }

    if (calcBtn) {
        calcBtn.addEventListener('click', () => {
            const debtRaw = document.getElementById('calc-debt').value.replace(/[^0-9.]/g, '');
            const termYears = parseInt(calcTermSlider.value, 10);
            const rateRaw = document.getElementById('calc-rate').value.replace(/[^0-9.]/g, '');

            const debt = parseFloat(debtRaw);
            const rate = parseFloat(rateRaw);

            if (isNaN(debt) || isNaN(rate) || isNaN(termYears) || debt <= 0 || rate <= 0 || termYears <= 0) {
                alert('Please enter valid positive numbers for all fields.');
                return;
            }

            const monthlyRate = (rate / 100) / 12;
            const totalMonths = termYears * 12;

            // Interest Only
            const ioMonthly = (debt * (rate / 100)) / 12;
            const ioTotal = ioMonthly * totalMonths;

            // Repayment (annuity formula)
            const rpMonthly = debt * (monthlyRate * Math.pow(1 + monthlyRate, totalMonths)) /
                (Math.pow(1 + monthlyRate, totalMonths) - 1);
            const rpTotal = rpMonthly * totalMonths;

            // Format as GBP
            const fmt = (n) => '£' + n.toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

            document.getElementById('res-io-monthly').textContent = fmt(ioMonthly);
            document.getElementById('res-io-total').textContent = fmt(ioTotal);
            document.getElementById('res-rp-monthly').textContent = fmt(rpMonthly);
            document.getElementById('res-rp-total').textContent = fmt(rpTotal);

            document.getElementById('calc-results').classList.add('visible');
        });
    }

    // ---- Subtle Hero Parallax ----
    const heroVisuals = document.querySelectorAll('.hero-panel-img, .hero-panel-right .hero-video');
    if (heroVisuals.length && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        let ticking = false;
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const y = window.scrollY;
                    if (y < window.innerHeight) {
                        heroVisuals.forEach(el => {
                            el.style.transform = 'translateY(' + (y * 0.15) + 'px) scale(1.05)';
                        });
                    }
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
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
