# -*- coding: utf-8 -*-
from core.config import SiteConfig
from generators.asset_manager import AssetManager
from generators.navigation import NavigationBuilder
from generators.pages import PageGenerator


class SiteGenerator:
    """Main site generator that orchestrates the build process."""
    
    def __init__(self, config_path: str = 'config.yaml', output_dir: str = 'site'):
        self.config = SiteConfig(config_path)
        self.output_dir = output_dir
        self.asset_manager = AssetManager(output_dir)
        self.nav_builder = NavigationBuilder(self.config.pages)
    
    def generate(self, paginate_by: int = 10) -> None:
        """
        Generate the complete static site.
        
        Args:
            paginate_by: Number of items per list page
        """
        print(f"Generating website: {self.config.site_title}")
        print(f"Output directory: {self.output_dir}")
        
        # Step 1: Generate assets
        print("Generating assets...")
        self.asset_manager.generate_all_assets(self.config.theme)
        
        # Step 2: Build navigation
        print("Building navigation...")
        nav = self.nav_builder.build_navigation()
        
        # Step 3: Initialize page generator
        page_generator = PageGenerator(
            output_dir=self.output_dir,
            site_title=self.config.site_title,
            base_url=self.config.base_url,
            nav=nav
        )
        
        # Step 4: Generate homepage
        print("Generating homepage...")
        page_generator.generate_homepage(self.config.homepage)
        
        # Step 5: Generate other pages
        print("Generating pages...")
        for page_config in self.config.pages:
            page_title = page_config.get('title', 'Untitled')
            path = page_config.get('path', '')
            
            # Check if it's an external URL
            if path.lower().startswith(('http://', 'https://')):
                print(f"  - {page_title} (external link)")
            else:
                print(f"  - {page_title}")
            
            page_generator.generate_page(page_config, paginate_by)

        print("Generation complete!")


def generate_site(config_path: str = 'config.yaml', output_dir: str = 'site', paginate_by: int = 10) -> None:
    """
    Convenience function to generate a site.
    
    Args:
        config_path: Path to the configuration file
        output_dir: Output directory for the generated site
        paginate_by: Number of items per list page
    """
    generator = SiteGenerator(config_path, output_dir)
    generator.generate(paginate_by)
