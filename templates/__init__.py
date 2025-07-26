# -*- coding: utf-8 -*-
"""
Templates module for the static site generator.
"""

from .base_template import BASE_TEMPLATE
from .page_template import PAGE_TEMPLATE
from .list_template import LIST_TEMPLATE
from .assets import CSS_TEMPLATE, JS_TEMPLATE

TEMPLATES = {
    'base.html': BASE_TEMPLATE,
    'page.html': PAGE_TEMPLATE,
    'list.html': LIST_TEMPLATE,
    'assets/style.css': CSS_TEMPLATE,
    'assets/script.js': JS_TEMPLATE
}

__all__ = [
    'TEMPLATES',
    'BASE_TEMPLATE',
    'PAGE_TEMPLATE', 
    'LIST_TEMPLATE',
    'CSS_TEMPLATE',
    'JS_TEMPLATE'
]
