#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autosite: Static site generator main entry point.
This module provides the command-line interface for the static site generator.
"""

from site_generator import generate_site


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate a static site from markdown.')
    parser.add_argument('--config', default='config.yaml', help='Path to config file')
    parser.add_argument('--output', default='site', help='Output directory')
    parser.add_argument('--paginate-by', type=int, default=10, help='Items per list page')
    args = parser.parse_args()
    generate_site(args.config, args.output, args.paginate_by)
