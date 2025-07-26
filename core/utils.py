# -*- coding: utf-8 -*-
"""
Utility functions for the static site generator.
"""
import re
from typing import Optional


def slugify(value: str) -> str:
    """
    Simple slugify function.
    
    Args:
        value: String to slugify
        
    Returns:
        Slugified string suitable for URLs
    """
    return ''.join(c if c.isalnum() else '-' for c in value.lower()).strip('-')


def extract_first_h1(md_content: str) -> Optional[str]:
    """
    Extract the first H1 heading from markdown content.
    
    Args:
        md_content: Markdown content to parse
        
    Returns:
        First H1 heading text or None if not found
    """
    # Look for # heading at the start of a line
    match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None
