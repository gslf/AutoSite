# -*- coding: utf-8 -*-
"""
List template for content listings with pagination.
"""

LIST_TEMPLATE = '''{% extends 'base.html' %}
{% block content %}
<section class="fade-in">
    <ul class="content-list">
    {% for item in items %}
        <li><a href="{{ base_url }}{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
    </ul>
    <div class="pagination">
        {% if prev_url %}
        <a href="{{ base_url }}{{ prev_url }}" class="prev">Previous</a>
        {% endif %}
        {% if next_url %}
        <a href="{{ base_url }}{{ next_url }}" class="next">Next</a>
        {% endif %}
    </div>
</section>
{% endblock %}'''
