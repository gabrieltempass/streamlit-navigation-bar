import os

import streamlit.components.v1 as components


_RELEASE = False

if not _RELEASE:
    _st_navbar = components.declare_component(
        "st_navbar",
        url="http://localhost:5173",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _st_navbar = components.declare_component(
        "st_navbar",
        path=build_dir,
    )


def st_navbar(pages, default="Home", logo_svg=None, logo_page="Home", key=None):
    page = _st_navbar(
        pages=pages,
        logo_svg=logo_svg,
        logo_page=logo_page,
        key=key,
        default=default
    )
    return page

