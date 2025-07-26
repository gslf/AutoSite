# -*- coding: utf-8 -*-
"""
Navigation builder for the static site generator.
"""
import os
from typing import List, Dict, Any

from core.utils import slugify


class NavigationBuilder:
    """Builds navigation structure for the site."""
    
    def __init__(self, pages_config: List[Dict[str, Any]]):
        self.pages_config = pages_config
    
    def build_navigation(self) -> List[Dict[str, str]]:
        """
        Build navigation structure from pages configuration.
        
        Returns:
            List of navigation items with title and url
        """
        nav = [{'title': 'Home', 'url': 'index.html'}]
        
        for page in self.pages_config:
            title = page.get('title') or os.path.splitext(os.path.basename(page['path']))[0].title()
            path = page['path']
            
            # Check if it's an external URL (starts with http:// or https://)
            if path.lower().startswith(('http://', 'https://')):
                nav.append({'title': title, 'url': path, 'external': True})
            else:
                slug = slugify(title)
                if os.path.isfile(path):
                    nav.append({'title': title, 'url': f'{slug}.html'})
                else:
                    nav.append({'title': title, 'url': f'{slug}/index.html'})
        
        return nav
