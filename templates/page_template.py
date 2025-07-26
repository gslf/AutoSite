# -*- coding: utf-8 -*-
"""
Page template for individual content pages.
"""

PAGE_TEMPLATE = '''{% extends 'base.html' %}
{% block content %}
<article class="fade-in">
    {{ content|safe }}
</article>
{% endblock %}'''
