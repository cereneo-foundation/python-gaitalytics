# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from importlib.metadata import version
release = version("gaitalytics")
#version = ".".join(release.split(".")[:2])
version = release

project = 'gaitalytics'
copyright = '2024, André Böni'
author = 'André Böni'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx_codeautolink',
              'sphinxcontrib.bibtex',
              'sphinx.ext.napoleon',
              'sphinxcontrib.mermaid',]

bibtex_bibfiles = ['_static/Gaitalytics.bib']

bibtex_encoding = 'utf-8'
# bibtex_reference_style = "author_year"
# bibtex_default_style = "plain"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'prev_next_buttons_location': 'bottom',
}

html_favicon = '_static/favicon.png'


napoleon_google_docstring = True
napoleon_include_init_with_doc = True

