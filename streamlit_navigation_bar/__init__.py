import os
import re
import base64

import streamlit as st
import streamlit.components.v1 as components


_RELEASE = True

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


def _encode_svg(svg):
    """Encode the given SVG string to base64."""
    return base64.b64encode(svg.encode("utf-8")).decode("utf-8")


def _adjust_html(html):
    """Make multiple HTML adjustments with st.markdown."""
    for key in html:
        st.markdown(html[key], unsafe_allow_html=True)


def _parse_html_to_dict(html):
    """Parse a HTML file to a Python dictionary."""
    chunks = re.split(r"\n\s*\n", html)
    dictionary = {}

    for chunk in chunks:
        _, key, value = re.split(r"(<!--\s.*\s-->\n)", chunk)
        key = re.split(r"\s", key)[1]
        dictionary[key] = value

    return dictionary

def st_navbar(
    pages,
    selected=None,
    logo_path=None,
    logo_page="Home",
    styles=None,
    adjust_html=True,
    key=None,
):
    """
    Place a navigation bar in your Streamlit app.
    
    If there is no st.set_page_config command on the app page, st_navbar must
    be the first Streamlit command used, and must only be set once per page.
    If there is a st.set_page_config command, then st_navbar must be the
    second one, right after it.

    Parameters
    ----------
    pages : list of str
        A list with the name of each page that will be displayed in the
        navigation bar.
    selected : str, optional
        The page that will be selected by default when the navigation bar is
        displayed. It could be one of the pages list values, but it is not
        limited to them.
    logo_path : str, optional
        The path to an SVG file for a logo. It will be shown on the left side
        of the navigation bar. Defaults to None, where no logo is displayed.
    logo_page : str, default="Home"
        Set the page value that will be returned by clicking on the logo (if
        there is one). For a non-clickable logo, set this to None.
    styles : dict of str: dict of str: str, optional
        A dictionary with the HTML tag name as the key and another dictionary
        to style it as the value. In the second dictionary, the key is a CSS
        property and the value is the value it will receive. The available
        HTML tags, and their respective structure order, are: "nav", "div",
        "ul", "li", "a", "img" and "selected". The last one is a custom tag to
        direct the styling just to the "a" element selected.
    adjust_html : bool, default=True
        By default, Streamlit limits the position of components in the web app
        to a certain width and adds a padding to the top. When this argument
        is set to True it adjusts the HTML for the navbar to be displayed at
        the full width and at the top of the screen, among other things (like
        hidding some Streamlit UI elements). In most cases, the HTML
        adjustment will not interfere with the rest of the web app, however
        there could be some situations where this occurs. If this happens,
        toggle `adjust_html` to False and make your own HTML adjustments with
        st.markdown.
    key : str or int, optional
        A string or integer to use as a unique key for the component. If this
        is omitted, a key will be generated for the widget based on its
        content. Multiple navbars of the same type may not share the same key.

    Returns
    -------
    page : str
        The selected page from the navigation bar. If there is no user
        interaction yet, returns the selected default value, else, returns the
        page clicked by the user.

    Examples
    --------
    >>> from streamlit_navigation_bar import st_navbar
    >>> pages = ["Home", "Documentation", "Blog", "About", "User"]
    >>> styles = {"nav": {"background-color": "black"}}
    >>> st_navbar(pages, selected="Home", styles=styles)
    """

    if logo_path is not None:
        base64_svg = _encode_svg(open(logo_path).read())

    page = _st_navbar(
        pages=pages,
        default=selected,
        base64_svg=base64_svg,
        logo_page=logo_page,
        styles=styles,
        key=key,
    )

    if adjust_html:
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(parent_dir, "adjustments.html")
        html = open(html_path).read()
        _adjust_html(_parse_html_to_dict(html))

    return page

