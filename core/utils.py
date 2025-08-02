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


def extract_first_h2(md_content: str) -> Optional[str]:
    """
    Extract the first H2 heading from markdown content.
    
    Args:
        md_content: Markdown content to parse
        
    Returns:
        First H2 heading text or None if not found
    """
    # Look for ## heading at the start of a line
    match = re.search(r'^## (.+)$', md_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def extract_order_number(filename: str) -> int:
    """
    Extract the order number from a filename with format 'number-name.ext'.
    
    Args:
        filename: Filename to parse (with or without path)
        
    Returns:
        Order number or 999999 if no number found (for sorting at the end)
    """
    basename = re.split(r'[/\\]', filename)[-1]  # Get just the filename
    match = re.match(r'^(\d+)-', basename)
    if match:
        return int(match.group(1))
    return 999999  # High number for files without order prefix


def remove_order_prefix(filename: str) -> str:
    """
    Remove the order prefix from a filename (number and dash).
    
    Args:
        filename: Filename to clean
        
    Returns:
        Filename without the order prefix
    """
    return re.sub(r'^\d+-', '', filename)
