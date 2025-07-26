<div align="center">

# 🚀 AutoSite

### A Modern Markdown-Based Static Site Generator

*Transform Markdown content into beautiful, responsive websites with zero configuration*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-black.svg)](https://github.com/psf/black)

---

</div>

## ✨ Features

- **🔥 Zero Configuration** - Get started with a single command
- **📝 Markdown-Powered** - Write content in clean, simple Markdown
- **🎨 Minimal Themes** - Customizable colors and fonts
- **📱 Mobile Responsive** - Looks perfect on all devices
- **⚡ Lightning Fast** - Generates sites in milliseconds
- **🗂️ Smart Navigation** - Automatic menu generation from your content
- **📄 Pagination** - Built-in pagination for blog posts and collections
- **🔗 External Links** - Seamlessly integrate external resources
- **🎯 SEO Ready** - Clean HTML structure optimized for search engines
- **🌙 Modern Design** - Clean, professional aesthetic with smooth animations

## 🖼️ Demo


![AutoSite Demo](assets/demo.gif)
*Screenshot showing a generated website with custom theme and navigation*

## 🚀 Quick Start

Get your static site running in under 2 minutes:

### 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

### 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gslf/AutoSite.git
   cd AutoSite
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate your first site**
   ```bash
   python gen.py
   ```

4. **View your site**
   Open `site/index.html` in your browser or serve it locally:
   ```bash
   # Using Python's built-in server
   cd site
   python -m http.server 8000
   ```
   
   Navigate to `http://localhost:8000` to see your site! 🎉

## 📁 Project Structure

```
AutoSite/
├── 📄 config.yaml          # Site configuration
├── 🐍 gen.py              # Main generator script
├── 📝 content/            # Your content files
│   ├── home.md           # Homepage content
│   ├── about.md          # About page
│   └── blog/             # Blog posts directory
│       ├── post1.md
│       ├── post2.md
│       └── ...
├── 🎨 assets/             # Custom assets (fonts, images)
├── 🏗️ templates/          # HTML templates
├── 🔧 core/               # Core functionality
├── ⚙️ generators/         # Content generators
└── 🌐 site/               # Generated website (output)
```

## ⚙️ Configuration

Customize your site by editing `config.yaml`:

```yaml
# Website title
title: "My Awesome Site"

# Base URL (for subdirectories)
base_url: "/my-site"

# Theme customization
theme:
  font_family: "'Inter', 'Arial', sans-serif"
  primary_color: "#3b82f6"
  contrast_color: "#1e40af"

# Homepage content
homepage: "content/home.md"

# Navigation pages
pages:
  - title: "About"
    path: "content/about.md"
  
  - title: "Blog"
    path: "content/blog"
  
  - title: "GitHub"
    path: "https://github.com/username"
```

### 🎯 Configuration Options

| Option | Description | Example |
|--------|-------------|---------|
| `title` | Site title shown in header and browser tabs | `"My Blog"` |
| `base_url` | Base URL for hosting in subdirectories | `"/blog"` |
| `homepage` | Path to homepage Markdown file | `"content/home.md"` |
| `theme.font_family` | CSS font family for the site | `"'Roboto', sans-serif"` |
| `theme.primary_color` | Primary color (hex) | `"#ff6b6b"` |
| `theme.contrast_color` | Accent color (hex) | `"#4ecdc4"` |


## 🎨 Theme customization


### 🎨 Custom Colors

```yaml
theme:
  primary_color: "#ff6b6b"    # Links, buttons, accents
  contrast_color: "#4ecdc4"   # Hover states, highlights
```

### 🔤 Custom Fonts

```yaml
theme:
  font_family: "'Poppins', 'Arial', sans-serif"
```

Add custom font files to the `assets/` directory and reference them in your CSS.

### 🎯 Advanced Customization

- **CSS**: Modify styles in `templates/assets.py`
- **HTML**: Edit templates in `templates/`
- **JavaScript**: Enhance interactivity in the JS template

## 🔧 Advanced Usage

### Custom Build Options

```bash
# Custom configuration file
python gen.py --config my-config.yaml

# Custom output directory
python gen.py --output dist/

# Custom pagination
python gen.py --paginate-by 5
```

### Programmatic Usage

```python
from site_generator import generate_site

# Generate with custom settings
generate_site(
    config_path='config.yaml',
    output_dir='build/',
    paginate_by=15
)
```


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

<div align="center">

**⭐ Star this repo if you find it useful!**

Made with ❤️ by [GSLF](https://gslf.it)

[Report Bug](https://github.com/gslf/AutoSite/issues) • [Request Feature](https://github.com/gslf/AutoSite/issues) • [Documentation](https://github.com/gslf/AutoSite/wiki)

</div>