# -*- coding: utf-8 -*-
"""
Asset management for the static site generator.
"""
import os
import shutil
from typing import Dict, Any
from jinja2 import Template

from templates import TEMPLATES


class AssetManager:
    """Manages static assets and CSS generation."""
    
    def __init__(self, output_dir: str, source_assets_dir: str = 'assets'):
        self.output_dir = output_dir
        self.source_assets_dir = source_assets_dir
        self.assets_output_dir = os.path.join(output_dir, 'assets')
    
    def setup_output_directory(self) -> None:
        """Create and prepare the output directory."""
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.assets_output_dir, exist_ok=True)
    
    def copy_custom_assets(self) -> None:
        """Copy custom assets from source assets folder."""
        if not os.path.exists(self.source_assets_dir):
            print(f"Cartella assets '{self.source_assets_dir}' non trovata")
            return
        
        print(f"Copiando assets da: {self.source_assets_dir}")
        for item in os.listdir(self.source_assets_dir):
            source_path = os.path.join(self.source_assets_dir, item)
            dest_path = os.path.join(self.assets_output_dir, item)
            
            if os.path.isfile(source_path):
                shutil.copy2(source_path, dest_path)
                if item.endswith(('.ttf', '.otf', '.woff', '.woff2')):
                    print(f"Copiato font: {item}")
                else:
                    print(f"Copiato asset: {item}")
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path)
                print(f"Copiata cartella asset: {item}")
    
    def generate_css(self, theme: Dict[str, str]) -> None:
        """Generate CSS file with theme variables."""
        css_template = Template(TEMPLATES['assets/style.css'])
        css_content = css_template.render(
            font_family=theme['font_family'],
            primary_color=theme['primary_color'],
            contrast_color=theme['contrast_color']
        )
        
        css_path = os.path.join(self.assets_output_dir, 'style.css')
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css_content)
    
    def generate_js(self) -> None:
        """Generate JavaScript file."""
        js_path = os.path.join(self.assets_output_dir, 'script.js')
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(TEMPLATES['assets/script.js'])
    
    def generate_all_assets(self, theme: Dict[str, str]) -> None:
        """Generate all assets (CSS, JS) and copy custom assets."""
        self.setup_output_directory()
        self.copy_custom_assets()
        self.generate_css(theme)
        self.generate_js()
