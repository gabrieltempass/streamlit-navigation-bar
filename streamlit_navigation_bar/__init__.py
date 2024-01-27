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


def st_navbar(name, key=None):
    component_value = _st_navbar(name=name, key=key, default=0)
    return component_value

