# -*- coding: utf-8 -*-
"""
Core module for the static site generator.
"""

from .config import SiteConfig
from .utils import slugify, extract_first_h1

__all__ = ['SiteConfig', 'slugify', 'extract_first_h1']
