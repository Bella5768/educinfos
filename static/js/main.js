// Mobile Menu Toggle
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const nav = document.querySelector('.nav');

if (mobileMenuBtn && nav) {
    mobileMenuBtn.addEventListener('click', () => {
        nav.classList.toggle('active');
        
        if (nav.classList.contains('active')) {
            nav.style.display = 'flex';
            nav.style.flexDirection = 'column';
            nav.style.position = 'absolute';
            nav.style.top = '100%';
            nav.style.left = '0';
            nav.style.right = '0';
            nav.style.background = 'white';
            nav.style.padding = '1rem';
            nav.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        } else {
            nav.style.display = '';
            nav.style.flexDirection = '';
            nav.style.position = '';
            nav.style.top = '';
            nav.style.left = '';
            nav.style.right = '';
            nav.style.background = '';
            nav.style.padding = '';
            nav.style.boxShadow = '';
        }
    });
}

// Smooth Scroll for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            
            // Close mobile menu if open
            if (nav && nav.classList.contains('active')) {
                nav.classList.remove('active');
                nav.style.display = '';
            }
        }
    });
});

// Contact Form Handling
const contactForm = document.querySelector('.contact-form form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(this);
        const data = Object.fromEntries(formData);
        
        // Simple validation
        if (!data.name || !data.email || !data.subject || !data.message) {
            alert('Veuillez remplir tous les champs du formulaire.');
            return;
        }
        
        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(data.email)) {
            alert('Veuillez entrer une adresse email valide.');
            return;
        }
        
        // Show success message (in production, this would send data to server)
        alert('Merci pour votre message ! Nous vous répondrons bientôt.');
        this.reset();
    });
}

// Subscribe Button Handling
const subscribeBtns = document.querySelectorAll('.btn-primary');
subscribeBtns.forEach(btn => {
    if (btn.textContent.trim() === "S'abonner") {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const email = prompt('Entrez votre adresse email pour vous abonner :');
            if (email) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (emailRegex.test(email)) {
                    alert('Merci pour votre abonnement ! Vous recevrez nos dernières actualités.');
                } else {
                    alert('Veuillez entrer une adresse email valide.');
                }
            }
        });
    }
});

// Add scroll effect to header
const header = document.querySelector('.header');
if (header) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = '0 1px 2px rgba(0, 0, 0, 0.05)';
        }
    });
}

// Animation on scroll (simple fade-in)
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.feature-card, .article-card, .about-feature').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});
