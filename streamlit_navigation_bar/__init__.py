import os
import base64

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
    check_adjust,
    check_key,
)


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


def _encode_svg(path):
    """Encode an SVG to base64, from an absolute path."""
    svg = open(path).read()
    return base64.b64encode(svg.encode("utf-8")).decode("utf-8")


def _prepare_urls(urls, pages):
    """Fill a dictionary with specified and not specified hrefs and targets."""
    if urls is None:
        urls = {}
    for page in pages:
        if page in urls:
            urls[page] = [urls[page], "_blank"]
        else:
            urls[page] = ["#", "_self"]
    return urls


def _prepare_adjust(adjust):
    """."""
    options = {
        "show_menu": True,
        "show_sidebar": True,
        "fixed_shadow": True,
    }
    for option in options:
        if isinstance(adjust, dict) and option in adjust:
            options[option] = adjust[option]
        elif isinstance(adjust, bool) and not adjust:
            options[option] = adjust
    return options


def get_path(directory):
    """Get the abs path for a directory in the same location as this file."""
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(parent_dir, directory)


def load_env(templates_path):
    """Load the Jinja environment from a given absolute path."""
    loader = FileSystemLoader(templates_path)
    return Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)


def _adjust(css):
    """Apply a CSS adjustment."""
    wrapped = "<style>" + css + "</style>"
    st.markdown(wrapped, unsafe_allow_html=True)


def stylized_container(key):
    """
    Insert a container into the app, which receives an iframe that does not
    render anything. Style this container using CSS and a unique key to remove
    the space added by Streamlit.

    Parameters
    ----------
    key : str or int or None
        A key associated with this container. This needs to be unique since all
        styles will be applied to the container with this key.

    Returns
    -------
    container : DeltaGenerator
        A container object. Elements can be added to this container using
        either the "with" notation or by calling methods directly on the
        returned object.
    """
    html = (
        f"""
        <style>
            div[data-testid='stVerticalBlock']:has(
                > div.element-container
                > div.stMarkdown
                > div[data-testid='stMarkdownContainer']
                > p
                > span.{key}
            ) > div:first-child {{
                margin-bottom: -1rem;
            }}
        </style>
        <span class='{key}'></span>
        """
    )

    container = st.container()
    container.markdown(html, unsafe_allow_html=True)
    return container


def adjust_css(styles, adjust, key, templates_path):
    """
    Apply CSS adjustments to display the navbar correctly.

    By default, Streamlit limits the position of components in the web app to
    a certain width and adds a padding to the top. This function receives two
    Jinja templates to adjust the CSS for the navbar to be displayed at the
    full width and at the top of the window, among other changes.

    One template must contain the adjustments that will be made regardless of
    whether the `adjust` toggle is ``True`` or ``False``, and another must
    contain the adjustments dependent on their toggle state.

    If there are Streamlit UI elements that are set to be shown, via the
    `adjust` parameter, the function also reduces the width of the navbar to
    expose the header, with the UI elements, that is below. Then, it styles the
    header and the elements to look seamless with the navbar.

    Parameters
    ----------
    styles : dict of str: dict of str: str
        Apply CSS styles to desired targets, through a dictionary with the HTML
        tag or pseudo-class name as the key and another dictionary to style it
        as the value. In the second dictionary, the key-value pair is the name
        of a CSS property and the value it takes. The keys and values must be
        strings.

        The available HTML tags are: ``"nav"``, ``"div"``, ``"ul"``, ``"li"``,
        ``"a"``, ``"img"`` and ``"span"``. To better understand the document
        tree, check the notes section.

        The available pseudo-classes are: ``"active"`` and ``"hover"``, which
        direct the styling to the ``"span"`` tag. The menu and sidebar buttons
        are only styled by ``"hover"`` (if they are set to ``True`` in
        `adjust`). Currently, ``"hover"`` only accepts two CSS properties, they
        are: ``"color"`` and ``"background-color"``.
    adjust : bool or dict of str: bool or None
        It makes a series of CSS adjustments and displays the navbar correctly,
        by overriding some Streamlit behaviors.

        It is possible to customize the adjustments with options that can be
        toggled on or off. To do that, pass a dictionary with the option as the
        key and a boolean as the value. The available options are:
        ``"show_menu"`` and ``"show_sidebar"``. To toggle all options to the
        same state, pass ``True`` or ``False`` to `adjust`. Note that it is
        still needed to have ``st.sidebar`` in the app to be able to show the
        sidebar button.

        In most cases, the CSS adjustments do not interfere with the rest of
        the web app, however there could be some situations where this occurs.
        If this happens, or it is desired to disable all of them, pass ``None``
        to `adjust` and, when necessary, make your own CSS adjustments with
        ``st.markdown``.
    key : str or int or None
        A key associated with this container. This needs to be unique since all
        styles will be applied to the container with this key.
    templates_path : str
        The absolute path to the directory containing the Jinja templates with
        the CSS adjustments. The directory must contain two templates, one
        named ``"base.css"`` with the adjustments that will be made regardless
        of whether the `adjust` toggle is ``True`` or ``False``, and another
        named ``options.css``, that contains the adjustments dependent on their
        toggle state.

        The ``options.css`` template must have the CSS adjustments for each
        option inside a Jinja block, named after the respective option.
    """
    ui = MatchNavbar(styles, key)

    ui.height = ui.get_value(
        targets=["nav"],
        css_property="height",
        default="2.875rem",
    )
    ui.hover_bg_color = ui.get_value(
        targets=["hover"],
        css_property="background-color",
        default="transparent",
    )
    ui.color = ui.get_value(
        targets=["span"],
        css_property="color",
        option="textColor",
        default="rgb(49, 51, 63)",
    )
    ui.bg_color = ui.get_value(
        targets=["nav"],
        css_property="background-color",
        option="secondaryBackgroundColor",
        default="rgb(240, 242, 246)",
    )
    ui.hover_color = ui.get_value(
        targets=["hover", "span"],
        css_property="color",
        option="textColor",
        default="rgb(49, 51, 63)",
    )

    adjust = _prepare_adjust(adjust)
    margin = adjust["show_menu"] or adjust["show_sidebar"]
    key = f"st_navbar_key_{key}"

    env = load_env(templates_path)
    template = env.get_template("options.css")
    css = template.render(
        adjust=adjust,
        ui=ui,
        margin=margin,
        key=key,
    )
    with stylized_container(key=key):
        _adjust(css)


# A placeholder object to implement the default rules for selected
sentinel = object()


def st_navbar(
    pages,
    selected=sentinel,
    logo_path=None,
    logo_page="Home",
    urls=None,
    styles=None,
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
    urls : dict of str: str, optional
        A dictionary with the page name as the key and an external URL as the
        value, both as strings. The page name must be contained in the `pages`
        list. The URL will open in a new window or tab. The default is
        ``None``.
    styles : dict of str: dict of str: str, optional
        Apply CSS styles to desired targets, through a dictionary with the HTML
        tag or pseudo-class name as the key and another dictionary to style it
        as the value. In the second dictionary, the key-value pair is the name
        of a CSS property and the value it takes. The keys and values must be
        strings. Defaults to ``None``, where no custom style is applied.

        The available HTML tags are: ``"nav"``, ``"div"``, ``"ul"``, ``"li"``,
        ``"a"``, ``"img"`` and ``"span"``. To better understand the document
        tree, check the notes section.

        The available pseudo-classes are: ``"active"`` and ``"hover"``, which
        direct the styling to the ``"span"`` tag. The menu and sidebar buttons
        are only styled by ``"hover"`` (if they are set to ``True`` in
        `adjust`). Currently, ``"hover"`` only accepts two CSS properties, they
        are: ``"color"`` and ``"background-color"``.
    adjust : bool or dict of str: bool or None, default=True
        It makes a series of CSS adjustments and displays the navbar correctly,
        by overriding some Streamlit behaviors.

        It is possible to customize the adjustments with options that can be
        toggled on or off. To do that, pass a dictionary with the option as the
        key and a boolean as the value. The available options are:
        ``"show_menu"`` and ``"show_sidebar"``. To toggle all options to the
        same state, pass ``True``, which is the parameter default value, or
        ``False`` to `adjust`. Note that it is still needed to have
        ``st.sidebar`` in the app to be able to show the sidebar button.

        In most cases, the CSS adjustments do not interfere with the rest of
        the web app, however there could be some situations where this occurs.
        If this happens, or it is desired to disable all of them, pass ``None``
        to `adjust` and, when necessary, make your own CSS adjustments with
        ``st.markdown``.
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
    **Theme variables**

    The component accepts theme variables to be passed in the `styles`
    dictionary, as the values for the CSS properties, for example::
    
        styles = {
            "nav": {
                "background-color": "var(--primary-color)"
            }
        }
    
    The theme variables that can be used are::
    
        --primary-color
        --background-color
        --secondary-background-color
        --text-color
        --font

    By default, it uses the following theme variables to style ``"nav"``,
    ``"span"`` and ``"active"``::
    
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
    
    They can be overridden by simply passing another value to `styles`.

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
    between them. The default value is ``"700px"``, which works well
    in most cases. But if the navbar has a large number of pages, or longer
    names, it might be necessary to increase the maximum width. Conversely,
    whenever the navbar has few pages or short names, this value may need to
    be reduced.

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

    if adjust is not None:
        adjust_css(styles, adjust, key, get_path("templates"))

    return page
