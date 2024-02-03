# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(THIS_DIR))

sys.path.insert(0, ROOT_DIR)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "数値解析ノート"
copyright = "2021–2024, Kenta Kabashima. Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License"
author = "Kenta Kabashima"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

# settings of myst-nb
extensions += ["myst_nb"]  # This will automatically include myst_parser
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
]
nb_execution_mode = "cache"
nb_execution_cache_path = os.path.join(
    os.path.dirname(THIS_DIR), "build", "jupyter_cache"
)

# setting of mathjax
# Configuration in https://github.com/executablebooks/jupyter-book/issues/1528
mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML"
mathjax2_config = {
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "processEscapes": True,
        "ignoreClass": "document",
        "processClass": "math|output_area",
    },
    "TeX": {
        "macros": {
            "bm": ["{\\boldsymbol{#1}}", 1],
        },
    },
    "displayAlign": "center",
}

# setting of opengraph
# https://pypi.org/project/sphinxext-opengraph/
extensions += ["sphinxext.opengraph"]
ogp_site_url = "https://numanalnote.musicscience37.com/"
ogp_site_name = project

# setting of bibtex
# https://sphinxcontrib-bibtex.readthedocs.io/
extensions += ["sphinxcontrib.bibtex"]
bibtex_bibfiles = [os.path.join(ROOT_DIR, "numerical-analysis-note", "articles.bib")]
bibtex_default_style = "unsrt"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_orange_book_theme"
html_static_path = ["_static"]

html_title = project

html_theme_options = {
    "show_prev_next": False,
    "pygment_light_style": "gruvbox-light",
    "pygment_dark_style": "native",
    "repository_url": "https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-analysis-note",
    "use_repository_button": True,
}
