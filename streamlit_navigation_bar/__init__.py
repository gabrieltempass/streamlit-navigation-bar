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
    urls=None,
    styles=None,
    adjust_html=True,
    key=None,
):
    """
    Place a navigation bar in your Streamlit app.
    
    If there is no `st.set_page_config` command on the app page, `st_navbar`
    must be the first Streamlit command used, and must only be set once per
    page. If there is a `st.set_page_config` command, then `st_navbar` must be
    the second one, right after it.

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
        of the navigation bar. Defaults to `None`, where no logo is displayed.
    logo_page : str, default="Home"
        Set the page value that will be returned by clicking on the logo (if
        there is one). For a non-clickable logo, set this to `None`.
    urls : dict of str: str, optional
        A dictionary with the page name as the key and an external URL as the
        value. The page name must be contained in the `pages` list. The URL
        will open in a new window or tab.
    styles : dict of str: dict of str: str, optional
        A dictionary with the HTML tag name as the key and another dictionary 
        to style it as the value. In the second dictionary, the key is a CSS 
        property and the value is the value it will receive. The available HTML 
        tags are: `"nav"`, `"div"`, `"ul"`, `"li"`, `"a"`, `"img"`, `"span"` 
        and `"selected"`. The last one is a custom tag to direct the styling 
        just to the `"span"` element selected. To better understand the 
        structure hierarchy, check the notes section.
    adjust_html : bool, default=True
        By default, Streamlit limits the position of components in the web app
        to a certain width and adds a padding to the top. When this argument
        is set to `True` it adjusts the HTML for the navbar to be displayed at
        the full width and at the top of the screen, among other things (like
        hiding some Streamlit UI elements). In most cases, the HTML
        adjustment will not interfere with the rest of the web app, however
        there could be some situations where this occurs. If this happens,
        toggle `adjust_html` to `False` and make your own HTML adjustments with
        `st.markdown`.
    key : str or int, optional
        A string or integer to use as a unique key for the component. If this
        is omitted, a key will be generated for the widget based on its
        content. Multiple navbars of the same type may not share the same key.

    Returns
    -------
    page : str or None
        The selected page from the navigation bar. If there is no user
        interaction yet, returns the selected default value, else, returns the
        page clicked by the user.

    Notes
    -----

    Theme variables

    The component uses by default two CSS variables from the web app's theme,
    to style the <nav> tag. They are:

    nav {
      font-family: var(--font);
      background-color: var(--primary-color);
    }

    It also accepts the theme variables to be passed in the style dictionary,
    as the values for the CSS properties, for example:

    styles = {
        "span": {"text-color": "--text-color"}
    }

    The theme variables that could be used are:

    --primary-color
    --background-color
    --secondary-background-color
    --text-color
    --font

    To style the navigation bar, it is important to understand its HTML
    structure hierarchy. Let us take a scenario where the navbar was created
    with pages=["Page one name", "Page two name"] and an SVG logo. On the
    frontend side, the component will build this structure (simplified for the
    explanation):

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
                Page one name
              </span>
            </a>
          </li>
          <li>
            <a>
              <span>
                Page two name
              </span>
            </a>
          </li>
        </ul>
      </div>
    </nav>

    Looking at the hierarchy it is possible to notice that the <a> tag will
    style both the logo and the strings. However, the <img> tag is unique to
    the logo, just as <span> is to the strings.

    A fundamental CSS property to adjust is the `max-width` for the `<div>` 
    tag. That is because it controls how much space the page names will have. 
    The default value is `700px`, which works well in most cases. But if the 
    navbar has a large number of pages, or longer names, it might be necessary 
    to increase the maximum width. Conversely, whenever the navbar has few 
    pages and short names, this value may need to be reduced to avoid very
    large spaces between them.

    Examples
    --------
    >>> import streamlit as st
    >>> from streamlit_navigation_bar import st_navbar
    >>> pages = ["Documentation", "Examples", "Community", "GitHub"]
    >>> urls = {"GitHub": "https://github.com"}
    >>> styles = {"nav": {"background-color": "black"}}
    >>> page = st_navbar(pages, selected="Home", urls=urls, styles=styles)
    >>> st.write(page)
    """

    base64_svg = None
    if logo_path is not None:
        base64_svg = _encode_svg(open(logo_path).read())

    if urls is None:
        urls = {}
    for page in pages:
        if page in urls:
            urls[page] = [urls[page], "_blank"]
        else:
            urls[page] = ["#", "_self"]

    page = _st_navbar(
        pages=pages,
        default=selected,
        base64_svg=base64_svg,
        logo_page=logo_page,
        urls=urls,
        styles=styles,
        key=key,
    )

    if adjust_html:
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(parent_dir, "adjustments.html")
        html = open(html_path).read()
        _adjust_html(_parse_html_to_dict(html))

    return page

