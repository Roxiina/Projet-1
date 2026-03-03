"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
project = "Projet 1"
copyright = "2026, Projet 1 Contributors"
author = "Projet 1 Contributors"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",  # Génération automatique depuis les docstrings
    "sphinx.ext.napoleon",  # Support pour les docstrings Google et NumPy
    "sphinx.ext.viewcode",  # Liens vers le code source
    "sphinx.ext.intersphinx",  # Liens vers d'autres documentations
    "sphinx.ext.todo",  # Support pour les TODO
    "sphinx.ext.coverage",  # Rapport de couverture de la documentation
    "myst_parser",  # Support pour Markdown
    "sphinx_design",  # Grids, cards, tabs pour une meilleure UI
    "sphinx_copybutton",  # Bouton copier pour les blocs de code
]

# Napoleon settings pour les docstrings au format Google
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2563eb",
        "color-brand-content": "#1e40af",
        "color-api-name": "#0ea5e9",
        "color-api-pre-name": "#0891b2",
        "color-link": "#2563eb",
        "color-link--hover": "#1e40af",
    },
    "dark_css_variables": {
        "color-brand-primary": "#60a5fa",
        "color-brand-content": "#93c5fd",
        "color-api-name": "#38bdf8",
        "color-api-pre-name": "#06b6d4",
        "color-link": "#60a5fa",
        "color-link--hover": "#93c5fd",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
    "announcement": (
        "🚀 Bienvenue dans la documentation du Projet 1 - "
        "Template moderne pour vos projets IA!"
    ),
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Roxiina/Projet-1",
            "html": (
                "<svg stroke=\"currentColor\" fill=\"currentColor\" "
                "stroke-width=\"0\" viewBox=\"0 0 16 16\">"
                "<path fill-rule=\"evenodd\" d=\"M8 0C3.58 0 0 3.58 0 8c0 "
                "3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82"
                "-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82"
                "-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 "
                "1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64"
                "-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08"
                "-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36"
                ".09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 "
                "2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29"
                ".25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55"
                ".38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z\"></path>"
                "</svg>"
            ),
            "class": "",
        },
    ],
}

html_title = "🎯 Projet 1 - Documentation"
html_short_title = "Projet 1"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for todo extension ----------------------------------------------
todo_include_todos = True

# -- MyST Parser configuration -----------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
    "tasklist",
]

# -- Autodoc configuration ---------------------------------------------------
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
