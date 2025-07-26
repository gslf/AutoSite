# -*- coding: utf-8 -*-
"""
Configuration management for static site generator.
"""
import yaml
from typing import Dict, List, Any


class SiteConfig:
    """Manages site configuration and theme settings."""
    
    def __init__(self, config_path: str = 'config.yaml'):
        self.config_path = config_path
        self._config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        try:
            with open(self.config_path, encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file '{self.config_path}' not found")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in configuration file: {e}")
    
    @property
    def site_title(self) -> str:
        """Get site title."""
        return self._config.get('title', 'SiteGen')
    
    @property
    def base_url(self) -> str:
        """Get base URL with proper formatting."""
        base_url = self._config.get('base_url', '')
        if base_url and not base_url.endswith('/'):
            base_url += '/'
        return base_url
    
    @property
    def homepage(self) -> str:
        """Get homepage markdown file path."""
        return self._config.get('homepage', 'content/home.md')
    
    @property
    def pages(self) -> List[Dict[str, Any]]:
        """Get pages configuration."""
        return self._config.get('pages', [])
    
    @property
    def theme(self) -> Dict[str, str]:
        """Get theme configuration with defaults."""
        theme = self._config.get('theme', {})
        return {
            'font_family': theme.get('font_family', 'var(--custom-font-family)'),
            'primary_color': theme.get('primary_color', '#667eea'),
            'contrast_color': theme.get('contrast_color', '#764ba2')
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key."""
        return self._config.get(key, default)
