"""Configuration file for Sphinx."""

# pylint: disable=invalid-name

import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(THIS_DIR))

sys.path.insert(0, ROOT_DIR)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "数値解析ノート"
copyright = (  # pylint: disable=redefined-builtin
    "2021–2025, Kenta Kabashima. "
    "Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License"
)
author = "Kenta Kabashima"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns: list[str] = []

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

# setting of MathJax
# Extension for MathJax is already enabled by myst_nb.
# MathJax URL working with Plotly was written in https://www.npmjs.com/package/plotly.js/v/3.0.1.
mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG.js"
mathjax_config = {
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
        "processClass": "math|output_area",
    },
    # MathJax2形式でマクロを追加
    "TeX": {
        "Macros": {
            "bm": ["{\\boldsymbol{#1}}", 1],
        },
    },
}

# setting of opengraph
# https://pypi.org/project/sphinxext-opengraph/
extensions += ["sphinxext.opengraph"]
ogp_site_url = "https://numanalnote.musicscience37.com/"
ogp_site_name = project
ogp_social_cards = {"enable": False}

# setting of bibtex
# https://sphinxcontrib-bibtex.readthedocs.io/
extensions += ["sphinxcontrib.bibtex"]
bibtex_bibfiles = [os.path.join(ROOT_DIR, "numerical-analysis-note", "articles.bib")]
bibtex_default_style = "unsrt"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_orange_book_theme"
html_static_path = ["_static"]

# Required for plotly.
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"
]

html_title = project

html_favicon = "../../icon-logo/icon.svg"

html_theme_options = {
    "logo": {
        "image_light": "../../icon-logo/logo.svg",
        "image_dark": "../../icon-logo/logo-dark.svg",
    },
    "show_prev_next": False,
    "pygments_light_style": "gruvbox-light",
    "pygments_dark_style": "native",
    "repository_url": "https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-analysis-note",
    "use_repository_button": True,
}
