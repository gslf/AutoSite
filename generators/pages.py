# -*- coding: utf-8 -*-
"""
Page generation for the static site generator.
"""
import os
import glob
from typing import List, Dict, Any
import markdown
from jinja2 import Environment, DictLoader, select_autoescape

from templates import TEMPLATES
from core.utils import slugify, extract_first_h1, extract_first_h2


class PageGenerator:
    """Generates HTML pages from markdown content."""
    
    def __init__(self, output_dir: str, site_title: str, base_url: str, nav: List[Dict[str, str]]):
        self.output_dir = output_dir
        self.site_title = site_title
        self.base_url = base_url
        self.nav = nav
        self.env = self._setup_jinja_environment()
    
    def _setup_jinja_environment(self) -> Environment:
        """Set up Jinja2 environment with templates."""
        return Environment(
            loader=DictLoader({
                'base.html': TEMPLATES['base.html'],
                'page.html': TEMPLATES['page.html'],
                'list.html': TEMPLATES['list.html'],
            }),
            autoescape=select_autoescape(['html', 'xml'])
        )
    
    def _extract_page_metadata(self, md_content: str, fallback_title: str) -> Dict[str, str]:
        """Extract metadata (title and description) from markdown content."""
        title = extract_first_h1(md_content)
        if not title:
            title = fallback_title.replace('-', ' ').title()
        
        description = extract_first_h2(md_content)
        if not description:
            description = ""
        
        return {
            'title': title,
            'description': description
        }
    
    def generate_homepage(self, homepage_path: str) -> None:
        """Generate the homepage from markdown."""
        with open(homepage_path, encoding='utf-8') as f:
            raw = f.read()
        
        # Extract metadata
        metadata = self._extract_page_metadata(raw, 'Home')
        
        html = markdown.markdown(raw, extensions=['fenced_code'])
        rendered = self.env.get_template('page.html').render(
            site_title=self.site_title, 
            page_title=metadata['title'], 
            page_description=metadata['description'],
            content=html,
            nav=self.nav, 
            current_url='index.html', 
            base_url=self.base_url
        )
        
        output_path = os.path.join(self.output_dir, 'index.html')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered)
    
    def generate_single_page(self, page_config: Dict[str, Any]) -> None:
        """Generate a single page from markdown."""
        title = page_config.get('title') or os.path.splitext(os.path.basename(page_config['path']))[0].title()
        slug = slugify(title)
        path = page_config['path']
        
        if not os.path.isfile(path):
            print(f"Warning: File '{path}' not found.")
            return
        
        with open(path, encoding='utf-8') as f:
            raw = f.read()
        
        # Extract metadata
        metadata = self._extract_page_metadata(raw, title)
        
        html = markdown.markdown(raw, extensions=['fenced_code'])
        rendered = self.env.get_template('page.html').render(
            site_title=self.site_title, 
            page_title=metadata['title'],
            page_description=metadata['description'],
            content=html, 
            nav=self.nav, 
            current_url=f'{slug}.html', 
            base_url=self.base_url
        )
        
        output_path = os.path.join(self.output_dir, f'{slug}.html')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered)
    
    def generate_directory_pages(self, page_config: Dict[str, Any], paginate_by: int = 10) -> None:
        """Generate pages from a directory of markdown files with pagination."""
        title = page_config.get('title') or os.path.splitext(os.path.basename(page_config['path']))[0].title()
        slug = slugify(title)
        path = page_config['path']
        
        if not os.path.isdir(path):
            print(f"Warning: Directory '{path}' not found.")
            return
        
        files = sorted(glob.glob(os.path.join(path, '*.md')))
        items = []
        
        # Generate individual pages
        for md_file in files:
            name = os.path.splitext(os.path.basename(md_file))[0]
            page_slug = slugify(name)
            
            with open(md_file, encoding='utf-8') as f:
                raw = f.read()
            
            # Extract metadata
            metadata = self._extract_page_metadata(raw, name)
            
            content_html = markdown.markdown(raw, extensions=['fenced_code'])
            rendered = self.env.get_template('page.html').render(
                site_title=self.site_title, 
                page_title=metadata['title'],
                page_description=metadata['description'],
                content=content_html, 
                nav=self.nav,
                current_url=f'{slug}/{page_slug}.html', 
                base_url=self.base_url
            )
            
            out_dir = os.path.join(self.output_dir, slug)
            os.makedirs(out_dir, exist_ok=True)
            
            output_path = os.path.join(out_dir, f'{page_slug}.html')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(rendered)
            
            items.append({
                'title': metadata['title'], 
                'url': f'{slug}/{page_slug}.html',
                'description': metadata['description']
            })
        
        # Generate paginated list pages
        self._generate_paginated_list(items, title, slug, paginate_by)
    
    def _generate_paginated_list(self, items: List[Dict[str, str]], title: str, slug: str, paginate_by: int) -> None:
        """Generate paginated list pages for a collection."""
        total = len(items)
        pages_count = (total + paginate_by - 1) // paginate_by
        
        for i in range(1, pages_count + 1):
            start = (i - 1) * paginate_by
            end = start + paginate_by
            page_items = items[start:end]
            
            prev_url = f'{slug}/page{i-1}.html' if i > 2 else (f'{slug}/index.html' if i == 2 else None)
            next_url = f'{slug}/page{i+1}.html' if i < pages_count else None
            
            # Set page title and description for list pages
            page_title = title if i == 1 else f'{title} - Page {i}'
            page_description = f'{title} archive page' + (f' {i}' if i > 1 else '')
            
            rendered = self.env.get_template('list.html').render(
                site_title=self.site_title, 
                page_title=page_title,
                page_description=page_description,
                items=page_items, 
                nav=self.nav,
                current_url=f'{slug}/index.html',
                prev_url=prev_url, 
                next_url=next_url,
                base_url=self.base_url
            )
            
            out_file = os.path.join(self.output_dir, slug, 'index.html' if i == 1 else f'page{i}.html')
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(rendered)
    
    def _is_external_page(self, page_config: Dict[str, Any]) -> bool:
        """Check if a page is an external URL."""
        path = page_config.get('path', '')
        return path.lower().startswith(('http://', 'https://'))
    
    def generate_page(self, page_config: Dict[str, Any], paginate_by: int = 10) -> None:
        """Generate a page (single file or directory), or skip if external."""
        # Skip external pages - they're only included in navigation
        if self._is_external_page(page_config):
            return
            
        path = page_config['path']
        
        if os.path.isfile(path):
            self.generate_single_page(page_config)
        elif os.path.isdir(path):
            self.generate_directory_pages(page_config, paginate_by)
        else:
            print(f"Warning: Path '{path}' not found.")
