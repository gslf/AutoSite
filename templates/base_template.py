# -*- coding: utf-8 -*-
"""
Base HTML template for the site.
"""

BASE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }} - {{ site_title }}</title>
    <link rel="stylesheet" href="{{ base_url }}assets/custom-font.css">
    <link rel="stylesheet" href="{{ base_url }}assets/style.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github.min.css">
</head>
<body>
    <header>
        <div class="container">
            <h1 class="logo"><a href="{{ base_url }}index.html">{{ site_title }}</a></h1>
            <button class="menu-toggle">☰</button>
            <nav>
                <ul>
                    {% for p in nav %}
                    <li{% if p.url == current_url %} class="active"{% endif %}>
                        {% if p.external %}
                        <a href="{{ p.url }}" target="_blank" rel="noopener noreferrer">{{ p.title }}</a>
                        {% else %}
                        <a href="{{ base_url }}{{ p.url }}">{{ p.title }}</a>
                        {% endif %}
                    </li>
                    {% endfor %}
                </ul>
            </nav>
        </div>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <script src="{{ base_url }}assets/script.js"></script>
    <script>hljs.highlightAll();</script>
</body>
</html>'''
