import os
import base64

import streamlit as st
import streamlit.components.v1 as components
from streamlit.config import get_config_options
from jinja2 import FileSystemLoader, Environment
from jinja2.utils import concat

from streamlit_navigation_bar.errors import (
    check_pages,
    check_selected,
    check_logo_path,
    check_logo_page,
    check_urls,
    check_styles,
    check_adjust,
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


def get_path(directory):
    """Get the abs path for a directory in the same location as this file."""
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(parent_dir, directory)


def load_env(templates_path):
    """Load the Jinja environment from a given absolute path."""
    loader = FileSystemLoader(templates_path)
    return Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)


def _get_visibility(adjust, key):
    """Return if the option is visible or hidden, based on the user's input."""
    if isinstance(adjust, dict) and key in adjust:
        return "visible" if adjust[key] else "hidden"
    return "visible" if adjust else "hidden"


def _get_margin(adjust):
    """Return if a margin is needed for any visible Streamlit UI elements."""
    if (
        isinstance(adjust, bool)
        or ("show_menu" not in adjust)
        or ("show_sidebar" not in adjust)
        or ("show_menu" in adjust and adjust["show_menu"])
        or ("show_sidebar" in adjust and adjust["show_sidebar"])
    ):
        return True
    return False


def _adjust(css):
    """Prepare and apply a CSS adjustment."""
    wrapped = "<style>" + css + "</style>"
    st.markdown(wrapped, unsafe_allow_html=True)


def _get_style(styles, targets, css_property, default, option=None):
    """
    Get the value of a CSS property.

    Search for the right value in order to style seamlessly Streamlit's header
    and its UI elements, e.g. menu and sidebar buttons, with the navbar. First,
    it looks for a possible value defined via the `styles` dictionary. If there
    is not one, search the configuration options. If it still cannot be found,
    return a default value.

    Parameters
    ----------

    styles : dict of str: dict of str: str
        Apply CSS styles to desired targets, through a dictionary with the HTML
        tag or pseudo-class name as the key and another dictionary to style it
        as the value. In the second dictionary, the key-value pair is the name
        of a CSS property and the value it takes. The keys and values must be
        strings.
    targets : list of str
        The available HTML tags are: ``"nav"``, ``"div"``, ``"ul"``, ``"li"``,
        ``"a"``, ``"img"`` and ``"span"``. To better understand the document
        tree, check the notes section.

        The available pseudo-classes are: ``"active"`` and ``"hover"``, which
        direct the styling to the ``"span"`` tag. The menu and sidebar buttons
        are only styled by ``"hover"`` (if they are set to ``True`` in
        `adjust`). Currently, ``"hover"`` only accepts two CSS properties, they
        are: ``"color"`` and ``"background-color"``.

        The function searches for the value with the target that is in the
        first position of the list, if it does not find it, it iterates until
        the last item. When it finds the value, it returns it, even if there
        are still more targets in the list.
    css_property : str
        The name of the CSS property to get the value of.
    default : str
        The default value to be returned, in case the CSS property is not found
        in the styles dictionary or in the configurations.
    option : str, optional
        The name of the configuration option to get its value from. The
        configuration option could be in a TOML file for example.

    Returns
    -------
    value : str
        The value of the CSS property set via the styles dictionary,
        configuration option or default value.
    """
    value = None

    for target in targets:
        if styles is not None and target in styles:
            if css_property in styles[target]:
                return styles[target][css_property]

    if value is None and option is not None:
        value = get_config_options()[f"theme.{option}"].value
    
    if value is None:
        value = default

    return value


def adjust_css(styles, adjust, templates_path):
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
        to `adjust` and make your own CSS adjustments with ``st.markdown``.
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
    height = _get_style(styles, ["nav"], "height", "2.875rem")
    color = _get_style(styles, ["span"], "color", "white")
    hover_color = _get_style(styles, ["hover", "span"], "color", "white")
    bg_color = _get_style(
        styles, ["nav"], "background-color", "#ff4b4b", option="primaryColor"
    )
    hover_bg_color = _get_style(
        styles, ["hover"], "background-color", "transparent"
    )

    env = load_env(templates_path)

    position = 2
    options = env.get_template("options.css")
    for key, block_fun in options.blocks.items():

        visibility = _get_visibility(adjust, key)
        context_o = options.new_context(
            {
                "height": height,
                "color": color,
                "position": position,
                "visibility": visibility,
                "hover_color": hover_color,
                "hover_bg_color": hover_bg_color,
            }
        )
        _adjust(concat(block_fun(context_o)))
        position += 1

    margin = _get_margin(adjust)
    base = env.get_template("base.css")
    context_b = base.new_context(
        {
            "height": height,
            "bg_color": bg_color,
            "position": position,
            "margin": margin,
        }
    )
    _adjust(base.render(context_b))


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
        to `adjust` and make your own CSS adjustments with ``st.markdown``.
    key : str or int, optional
        A string or integer to use as a unique key for the component. If this
        is omitted, a key will be generated for the widget based on its
        content. Multiple navbars of the same type may not share the same key.

    Returns
    -------
    page : str or None
        The page selected by the user. If there has been no interaction yet,
        returns the preselected page or ``None``.

    Notes
    -----

    **Theme variables**

    The component uses by default two CSS variables from the web app's theme,
    to style the ``"nav"`` tag. They are::
    
        nav {
          font-family: var(--font);
          background-color: var(--primary-color);
        }
    
    It also accepts the theme variables to be passed in the `styles`
    dictionary, as the values for the CSS properties, for example::
    
        styles = {
            "span": {"color": "var(--text-color)"}
        }
    
    The theme variables that can be used are::
    
        --primary-color
        --background-color
        --secondary-background-color
        --text-color
        --font

    **Document tree**
    
    To style the navigation bar, it is important to understand its Document
    Object Model (DOM), also known as document tree. Take a scenario where the
    navbar was created with ``pages=["Hello, World!"]`` and an SVG logo. On the
    frontend side, the component will build this DOM (simplified for
    readability)::

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
    the pages names.

    **Maximum width**

    A fundamental CSS property to adjust is the ``"max-width"`` for the
    ``"div"`` tag. That is because it controls how much space the page names
    will have between them. The default value is ``"700px"``, which works well
    in most cases. But if the navbar has a large number of pages, or longer
    names, it might be necessary to increase the maximum width. Conversely,
    whenever the navbar has few pages or short names, this value may need to
    be reduced.

    Examples
    --------

    >>> import streamlit as st
    >>>
    >>> from streamlit_navigation_bar import st_navbar
    >>>
    >>> page = st_navbar(
    ...     ["Home", "Documentation", "Examples", "Community", "About"]
    ... )
    >>>
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
        adjust_css(styles, adjust, get_path("templates"))

    return page

