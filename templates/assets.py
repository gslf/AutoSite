# -*- coding: utf-8 -*-
"""
Asset templates (CSS and JavaScript).
"""

CSS_TEMPLATE = '''/* Variabili CSS personalizzabili */
:root {
    --font-family: {{ font_family }};
    --primary-color: {{ primary_color }};
    --contrast-color: {{ contrast_color }};
    --text-color: #2f2f2f;
    --bg-color: #ffffff;
    --border-color: rgba(0, 0, 0, 0.05);
    --shadow-color: rgba(0, 0, 0, 0.05);
    --gradient: linear-gradient(135deg, var(--primary-color) 0%, var(--contrast-color) 100%);
}

/* Reset & base */
* { 
    margin: 0; 
    padding: 0; 
    box-sizing: border-box; 
}

body { 
    font-family: var(--font-family); 
    color: var(--text-color); 
    line-height: 1.6; 
    background: var(--bg-color);
    min-height: 100vh;
}

.container { 
    max-width: 1000px; 
    margin: 0 auto; 
    padding: 1rem; 
}

img{
    max-width: 100%;
    height: auto;
    margin-bottom:40px;
    margin-top:20px;
}

/* Header & Navigation */
header { 
    background: rgba(255, 255, 255, 0.95); 
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border-color); 
    position: sticky; 
    top: 0; 
    z-index: 1000;
    box-shadow: 0 1px 10px var(--shadow-color);
    transition: all 0.3s ease;
}

h2{
    font-size: 1rem;
    margin-bottom: 45px;
}

header .container { 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    position: relative;
}

.logo a { 
    text-decoration: none; 
    color: var(--text-color); 
    font-size: 1.8rem; 
    font-weight: 700;
    transition: all 0.3s ease;
}

.logo a:hover {
    transform: scale(1.05);
}

/* Menu Toggle Button */
.menu-toggle { 
    display: none; 
    background: none; 
    border: none; 
    font-size: 1.8rem; 
    cursor: pointer;
    color: var(--text-color);
    padding: 0.5rem;
    border-radius: 8px;
    transition: all 0.3s ease;
    z-index: 1001;
    width: 80px;
    height: 30px;
    position: relative;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.menu-toggle span {
    display: block;
    width: 25px;
    height: 2px;
    background: var(--text-color);
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    position: relative;
}

.menu-toggle span:before,
.menu-toggle span:after {
    content: '';
    position: absolute;
    width: 25px;
    height: 2px;
    background: var(--text-color);
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.menu-toggle span:before {
    top: -8px;
}

.menu-toggle span:after {
    top: 8px;
}

.menu-toggle.active span {
    background: transparent;
}

.menu-toggle.active span:before {
    transform: rotate(45deg);
    top: 0;
}

.menu-toggle.active span:after {
    transform: rotate(-45deg);
    top: 0;
}

.menu-toggle:hover {
    transform: scale(1.1);
}

/* Navigation */
nav {
    position: relative;
}

nav ul { 
    list-style: none; 
    display: flex; 
    gap: 0.5rem;
    margin: 0;
    padding: 0;
}

nav li { 
    position: relative;
}

nav a { 
    text-decoration: none; 
    color: var(--text-color); 
    padding: 0.8rem 1.5rem;
    transition: all 0.3s ease;
    position: relative;
    font-weight: 500;
    display: block;
}

nav a::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 0;
    height: 2px;
    background: var(--gradient);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    transform: translateX(-50%);
}

nav a:hover::after,
nav .active a::after { 
    width: 80%;
}

nav a:hover { 
    color: var(--primary-color);
    transform: translateY(-2px);
}

/* Main Content */
main { 
    padding: 3rem 1rem; 
    background: rgba(255, 255, 255, 0.9);
    margin: 2rem auto;
    backdrop-filter: blur(10px);
    max-width: 1000px;
}

/* Animations */
.fade-in { 
    opacity: 0; 
    transform: translateY(30px); 
    transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
}

.fade-in.visible { 
    opacity: 1; 
    transform: none; 
}

/* Content styling */
.content-list { 
    list-style: none; 
}

.content-list li { 
    margin-bottom: 1rem;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 10px;
    transition: all 0.3s ease;
}

.content-list li:hover {
    transform: translateY(-3px);
    box-shadow: 0 3px 15px rgba(0, 0, 0, 0.05);
}

.content-list a {
    text-decoration: none;
    color: var(--text-color);
    font-weight: 500;
    transition: color 0.3s ease;
}

.content-list a:hover {
    color: var(--primary-color);
}

/* Pagination */
.pagination { 
    margin-top: 2rem; 
    text-align: center;
}

.pagination a { 
    margin: 0 0.5rem; 
    text-decoration: none; 
    padding: 0.8rem 1.5rem;
    background: var(--gradient);
    color: white;
    border-radius: 25px;
    transition: all 0.3s ease;
    display: inline-block;
}

.pagination a:hover {
    transform: translateY(-2px);
    box-shadow: 0 3px 10px color-mix(in srgb, var(--primary-color) 30%, transparent);
}

/* Mobile Styles */
@media (max-width: 768px) {
    .container {
        padding: 0.5rem;
    }
    
    .menu-toggle { 
        display: flex; 
        position: relative;
        z-index: 1001;
    }
    
    nav {
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        border-radius: 0 0 15px 15px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        transform: translateY(-20px);
        opacity: 0;
        visibility: hidden;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    nav.open {
        transform: translateY(0);
        opacity: 1;
        visibility: visible;
    }
    
    nav ul { 
        flex-direction: column; 
        padding: 1rem;
        gap: 0.5rem;
    }
    
    nav li {
        width: 100%;
    }
    
    nav a {
        width: 100%;
        text-align: center;
        padding: 1rem;
        margin: 0;
    }
    
    main {
        margin: 1rem auto;
        padding: 2rem 1rem;
    }
    
    .logo a {
        font-size: 1.5rem;
    }
}

/* Additional animations */
@keyframes slideInFromLeft {
    0% {
        transform: translateX(-100%);
        opacity: 0;
    }
    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes pulse {
    0%, 100% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.05);
    }
}

.logo a:hover {
    animation: pulse 0.6s ease-in-out;
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}

/* Link styles throughout the site */
a {
    text-decoration: none;
    transition: all 0.3s ease;
}

a:not(nav a):not(.logo a) {
    color: var(--primary-color);
    position: relative;
}

a:not(nav a):not(.logo a):hover {
    color: var(--contrast-color);
}

a:not(nav a):not(.logo a)::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--gradient);
    transition: width 0.3s ease;
}

a:not(nav a):not(.logo a):hover::after {
    width: 100%;
}
'''

JS_TEMPLATE = '''document.addEventListener('DOMContentLoaded', () => {
    // Hamburger menu with X transformation
    const btn = document.querySelector('.menu-toggle');
    const nav = document.querySelector('header nav');
    
    if (btn && nav) {
        // Create hamburger lines if they don't exist
        if (!btn.querySelector('span')) {
            btn.innerHTML = '<span></span>';
        }
        
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            nav.classList.toggle('open');
            btn.classList.toggle('active');
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!nav.contains(e.target) && !btn.contains(e.target)) {
                nav.classList.remove('open');
                btn.classList.remove('active');
            }
        });
        
        // Close menu when clicking on a nav link
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                nav.classList.remove('open');
                btn.classList.remove('active');
            });
        });
    }

    // Enhanced fade-in animation with stagger
    const faders = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 100); // Stagger animation
                observer.unobserve(entry.target);
            }
        });
    }, { 
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    faders.forEach(el => observer.observe(el));
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add scroll effect to header
    let lastScroll = 0;
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > lastScroll && currentScroll > 100) {
            header.style.transform = 'translateY(-100%)';
        } else {
            header.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });
    
    // Add loading animation to page
    document.body.style.opacity = '0';
    document.body.style.transform = 'translateY(20px)';
    
    setTimeout(() => {
        document.body.style.transition = 'all 0.6s ease';
        document.body.style.opacity = '1';
        document.body.style.transform = 'translateY(0)';
    }, 100);
});'''
