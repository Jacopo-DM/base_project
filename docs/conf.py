"""Sphinx configuration."""

html_theme = "shibuya"

project = "Example Project (to Learn)"

author = "jmdm"

copyright = "2025, jmdm"  # noqa: A001

extensions = [
    "myst_parser",
    "sphinx_design",
    "autodoc2",
    "sphinx.ext.napoleon",
]

# --------- SHIBUYA --------- #
templates_path = ["_templates"]
# html_title =
# html_logo =
# html_favicon =

# --------- MYST --------- #
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


# --------- AUTODOC2 --------- #
autodoc2_packages = [
    "../src/a2_base",
]
