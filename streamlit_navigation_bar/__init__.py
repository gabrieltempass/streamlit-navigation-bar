import os
import base64
from importlib.metadata import version as _version

import streamlit as st
import streamlit.components.v1 as components
from jinja2 import FileSystemLoader, Environment

from streamlit_navigation_bar.match_navbar import MatchNavbar
from streamlit_navigation_bar.errors import (
    check_pages,
    check_selected,
    check_logo_path,
    check_logo_page,
    check_urls,
    check_styles,
    check_options,
    check_adjust,
    check_key,
)


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


def print_version():
    """Show the installed version of the Streamlit Navigation Bar package."""
    version = _version("streamlit-navigation-bar")
    print(f"Streamlit Navigation Bar, version {version}")


def _encode_svg(path):
    """Encode an SVG to base64, from an absolute path."""
    svg = open(path).read()
    return base64.b64encode(svg.encode("utf-8")).decode("utf-8")


def _prepare_urls(urls, pages):
    """Build dict with given hrefs, targets and defaults where omitted."""
    if urls is None:
        urls = {}
    for page in pages:
        # Add {page: [href, target]} to the `urls` dict.
        if page in urls:
            urls[page] = [urls[page], "_blank"]
        else:
            urls[page] = ["#", "_self"]
    return urls


def _prepare_options(options):
    """Build dict with given options, state and defaults where omitted."""
    available = {
        "show_menu": True,
        "show_sidebar": True,
        "hide_nav": True,
        "fix_shadow": True,
        "use_padding": True,
    }
    for option in available:
        if isinstance(options, dict) and option in options:
            available[option] = options[option]
        elif isinstance(options, bool) and not options:
            available[option] = options
    return available


def _adjust(css):
    """Apply a CSS adjustment."""
    st.html("<style>" + css + "</style>")


def get_path(directory):
    """Get the abs path for a directory in the same location as this file."""
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(parent_dir, directory)


def load_env(path):
    """Load the Jinja environment from a given absolute path."""
    loader = FileSystemLoader(path)
    return Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)


def position_body(key, use_padding):
    """
    Add a stylized container to the app that adjusts the position of the body.

    Insert a container into the app, to add an ``st.html``, using either the
    "with" notation or by calling the method directly on the returned object.

    This container serves to position the body of the app in the y axis of the
    window. Which can be the same as the default in Streamlit (6rem from the
    top), or right below the navbar.

    It does so by having a unique CSS selector, and being inserted in a <div>
    palced immediately before the <div> of the body of the app. Then, it styles
    the margin-bottom property and moves the body to the desired position.

    Parameters
    ----------
    key : str, int or None
        A key associated with this container. This needs to be unique since all
        styles will be applied to the container with this key.

    Returns
    -------
    container : DeltaGenerator
        A container object. ``st.html`` can be added to this container using
        either the ``"with"`` notation or by calling methods directly on the
        returned object.
    """
    if use_padding:
        # The position of the body will be 6rem from the top.
        margin_bottom = "-4.875rem"
    else:
        # The position of the body will be right below the navbar.
        margin_bottom = "-8rem"

    html = (
        f"""
        <style>
            div[data-testid="stVerticalBlockBorderWrapper"]:has(
                div[data-testid="stVerticalBlock"]
                > div.element-container
                > div.stHtml
                > span.{key}
            ) {{
                margin-bottom: {margin_bottom};
            }}
        </style>
        <span class='{key}'></span>
        """
    )
    container = st.container()
    container.html(html)
    return container


def adjust_css(styles, options, key, path):
    """
    Apply CSS adjustments to display the navbar correctly.

    By default, Streamlit limits the position of components in the web app to
    a certain width and adds a padding to the top. This function renders Jinja
    templates to adjust the CSS and display the navbar at the full width at the
    top of the window, among other options that can be toggled on or off.

    It also matches the style, theme and configuration between the navbar and 
    Streamlit's User Interface (UI) elements, to make them look seamless.

    Parameters
    ----------
    styles : dict of {str : dict of {str : str}}
        Apply CSS styles to desired targets, through a dictionary with the HTML
        tag or pseudo-class name as the key and another dictionary to style it
        as the value. In the second dictionary, the key-value pair is the name
        of a CSS property and the value it takes. The keys and values must be
        strings.

        The available HTML tags are: ``"nav"``, ``"div"``, ``"ul"``, ``"li"``,
        ``"a"``, ``"img"`` and ``"span"``.

        The available pseudo-classes are: ``"active"`` and ``"hover"``, which
        direct the styling to the ``"span"`` tag. The menu and sidebar buttons
        are only styled by ``"hover"`` (if they are set to ``True`` in
        `options`). Currently, ``"hover"`` only accepts two CSS properties,
        they are: ``"color"`` and ``"background-color"``.
    options : bool or dict of {str : bool}
        Customize the navbar with options that can be toggled on or off. It
        accepts a dictionary with the option name as the key and a boolean as
        the value. The available options are: ``"show_menu"``,
        ``"show_sidebar"``, ``"hide_nav"``, ``"fix_shadow"`` and
        ``"use_padding"``.

        It is also possible to toggle all options to the same state. Simply
        pass ``True`` or ``False`` to `options`.
    key : str, int or None
        A key associated with the container that adjusts the CSS. This needs to
        be unique since all styles will be applied to the container with this
        key.
    path : str
        The absolute path to the directory containing the Jinja templates with
        the CSS adjustments.
    """
    ui = MatchNavbar(styles, key)

    ui.height = ui.get_value(
        css_property="height",
        targets=["nav"],
        default="2.875rem",
    )
    ui.hover_bg_color = ui.get_value(
        css_property="background-color",
        targets=["hover"],
        default="transparent",
    )
    ui.color = ui.get_value(
        css_property="color",
        targets=["span"],
        default="rgb(49, 51, 63)",
        theme_config="textColor",
    )
    ui.bg_color = ui.get_value(
        css_property="background-color",
        targets=["nav"],
        default="rgb(240, 242, 246)",
        theme_config="secondaryBackgroundColor",
    )
    ui.hover_color = ui.get_value(
        css_property="color",
        targets=["hover", "span"],
        default="rgb(49, 51, 63)",
        theme_config="textColor",
    )

    options = _prepare_options(options)
    margin = options["show_menu"] or options["show_sidebar"]
    key = f"st_navbar_key_{key}"

    env = load_env(path)
    template = env.get_template("options.css")
    css = template.render(
        ui=ui,
        options=options,
        margin=margin,
        key=key,
    )
    with position_body(key, options["use_padding"]):
        _adjust(css)


# A placeholder object to implement the default rules for `selected`.
sentinel = object()


def st_navbar(
    pages,
    selected=sentinel,
    logo_path=None,
    logo_page="Home",
    urls=None,
    styles=None,
    options=True,
    adjust=True,
    key=None,
):
    """
    Place a navigation bar in your Streamlit app.
    
    If there is no ``st.set_page_config`` command on the app page,
    ``st_navbar`` must be the first Streamlit command used, and must only be
    set once per page. If there is a ``st.set_page_config`` command, then
    ``st_navbar`` must be the second one, right after it.

    Parameters
    ----------
    pages : list of str
        A list with the name of each page that will be displayed in the
        navigation bar.
    selected : str or None, optional
        The preselected page on first render. It can be a name from `pages`,
        the `logo_page` (when there is a logo) or ``None``. Defaults to the
        `logo_page` value, if there is a logo. In case there is not one,
        defaults to the first page of the `pages` list. When set to ``None``,
        it will initialize empty and return ``None`` until the user selects a
        page.
    logo_path : str, optional
        The absolute path to an SVG file for a logo. It will be shown on the
        left side of the navigation bar. Defaults to ``None``, where no logo is
        displayed.
    logo_page : str or None, default="Home"
        The page value that will be returned when the logo is selected, if
        there is one. Defaults to ``"Home"``. For a non-clickable logo, set
        this to ``None``.
    urls : dict of {str : str}, optional
        A dictionary with the page name as the key and an external URL as the
        value, both as strings. The page name must be contained in the `pages`
        list. The URL will open in a new window or tab. The default is
        ``None``.
    styles : dict of {str : dict of {str : str}}, optional
        Apply CSS styles to desired targets, through a dictionary with the HTML
        tag or pseudo-class name as the key and another dictionary to style it
        as the value. In the second dictionary, the key-value pair is the name
        of a CSS property and the value it takes. The keys and values must be
        strings. Defaults to ``None``, where no custom style is applied.

        The available HTML tags are: ``"nav"``, ``"div"``, ``"ul"``, ``"li"``,
        ``"a"``, ``"img"`` and ``"span"``. To better understand the Document
        Object Model, check the notes section.

        The available pseudo-classes are: ``"active"`` and ``"hover"``, which
        direct the styling to the ``"span"`` tag. The menu and sidebar buttons
        are only styled by ``"hover"`` (if they are set to ``True`` in
        `options`). Currently, ``"hover"`` only accepts two CSS properties,
        they are: ``"color"`` and ``"background-color"``.
    options : bool or dict of {str : bool}, default=True
        Customize the navbar with options that can be toggled on or off. It
        accepts a dictionary with the option name as the key and a boolean as
        the value. The available options are: ``"show_menu"``,
        ``"show_sidebar"``, ``"hide_nav"``, ``"fix_shadow"`` and
        ``"use_padding"``. Check the API reference in the Notes section for a
        description of each one.

        It is also possible to toggle all options to the same state. Simply
        pass ``True`` to `options`, which is the parameter default value, or
        ``False``.
    adjust : bool, default=True
        When set to ``True`` (default), it overrides some Streamlit behaviors
        and makes a series of CSS adjustments to display the navbar correctly.

        In most cases, the CSS adjustments do not interfere with the rest of
        the web app, however there could be some situations where this occurs.
        If this happens, or it is desired to disable all of them, pass
        ``False`` to `adjust` and, when necessary, make your own CSS
        adjustments with ``st.html``.

        If set to ``False``, it will also disable all adjustments made by
        `options`, regardless of whether they are on or off.
    key : str or int, optional
        A string or integer to use as a unique key for the component. Multiple
        navbars may not share the same key. Defaults to ``None``.

    Returns
    -------
    page : str or None
        The page selected by the user. If there has been no interaction yet,
        returns the preselected page or ``None``.

    Notes
    -----
    **CSS variables**

    The component accepts theme configuration options to be passed as CSS
    variables in the `styles` dictionary, for example::
    
        styles = {
            "nav": {
                "background-color": "var(--primary-color)"
            }
        }
    
    The CSS variables that can be used are::
    
        --primary-color
        --background-color
        --secondary-background-color
        --text-color
        --font

    By default, the navbar uses in the following targets these CSS variables::
    
        styles = {
            "nav": {
                "font-family": "var(--font)",
                "background-color": "var(--secondary-background-color)"
            },
            "span": {
                "color": "var(--text-color)"
            },
            "active": {
                "color": "var(--text-color)"
            }
        }
    
    They can be overridden by simply passing another value to the respective
    target and CSS property in `styles`.

    **Document Object Model**
    
    To style the navigation bar, it is important to understand its Document
    Object Model (DOM). For example, if a navbar is created with
    ``pages=["Hello, World!"]`` and an SVG logo. On the frontend side, the
    component builds this DOM (simplified for readability)::

        <nav>
          <div>
            <ul>
              <li>
                <a>
                  <img src="svg_logo" img/>
                </a>
              </li>
              <li>
                <a>
                  <span>
                    Hello, World!
                  </span>
                </a>
              </li>
            </ul>
          </div>
        </nav>

    Notice that the ``"a"`` tag will style both the logo and the page name.
    However, the ``"img"`` tag is unique to the logo, just as ``"span"`` is to
    the page names.

    **Maximum width**

    A fundamental CSS property to adjust is the ``"max-width"`` for the
    ``"div"`` tag. Because it controls how much space the page names have
    between them. The default value is ``"43.75rem"``, which works well
    in most cases. But if the navbar has a large number of pages, or longer
    names, it might be necessary to increase the maximum width. Conversely,
    whenever the navbar has few pages or short names, this value may need to
    be reduced.

    **Options**

    The available options and their descriptions are:

    "show_menu"
        Show Streamlit's menu button in the navbar.
    "show_sidebar"
        Show Streamlit's sidebar button in the navbar. However, it is still
        needed to use ``st.sidebar`` in the app, in order for the sidebar
        button to properly appear. Just like Streamlit's default behavior.
    "fix_shadow"
        Fix the shadow of the expanded sidebar, showing it no matter the window
        width. It is useful when the navbar and the sidebar have the same
        background color, which they do by default, because the shadow makes it
        possible to differentiate between the two elements.

        When set to ``False``, it assumes Streamlit's default behavior, where
        it applies the shadow only when the window width is below a certain
        threshold.
    "use_padding"
        Position the body of the app, in the y axis of the window, 6rem from
        the top (if the navbar has a default height). This is the default style
        used by Streamlit. When set to ``False``, it removes this padding and
        positions the body right below the navbar.

    Examples
    --------
    >>> import streamlit as st
    >>> from streamlit_navigation_bar import st_navbar
    >>> page = st_navbar(
    ...     ["Home", "Documentation", "Examples", "Community", "About"]
    ... )
    >>> st.write(page)

    .. output::
       https://st-navbar-1.streamlit.app/
       height: 300px
    """
    check_pages(pages)
    check_selected(selected, logo_page, logo_path, pages)
    check_logo_path(logo_path)
    check_logo_page(logo_page)
    check_urls(urls, pages)
    check_styles(styles)
    check_options(options)
    check_adjust(adjust)
    check_key(key)

    if selected is sentinel:
        if logo_path is not None:
            default = logo_page
        else:
            default = pages[0]
    else:
        default = selected

    base64_svg = None
    if logo_path is not None:
        base64_svg = _encode_svg(logo_path)

    urls = _prepare_urls(urls, pages)

    page = _st_navbar(
        pages=pages,
        default=default,
        base64_svg=base64_svg,
        logo_page=logo_page,
        urls=urls,
        styles=styles,
        key=key,
    )

    if adjust:
        adjust_css(styles, options, key, get_path("templates"))

    return page
