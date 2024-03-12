# Streamlit Navigation Bar

A component that allows you to place a navigation bar in your
Streamlit app.

![Overview](https://github.com/gabrieltempass/streamlit-navigation-bar/raw/main/images/overview.gif)

## Installation

``` bash
pip install streamlit-navigation-bar
```

## Usage

If there is no [``st.set_page_config``](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)
command on the app page, ``st_navbar`` must be the first Streamlit command used,
and must only be set once per page. If there is a [``st.set_page_config``](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)
command, then ``st_navbar`` must be the second one, right after it.

## Parameters

**pages** : `list of str`</br>
A list with the name of each page that will be displayed in the navigation bar.

**selected** : `str` or `None`, optional</br>
The preselected page on first render. It can be a name from *pages*, the
*logo_page* (when there is a logo) or ``None``. Defaults to the *logo_page*
value, if there is a logo. In case there is not one, defaults to the first page
of the *pages* list. When set to ``None``, it will initialize empty and return
``None`` until the user selects a page.

**logo_path** : `str`, optional</br>
The absolute path to an SVG file for a logo. It will be shown on the left side
of the navigation bar. Defaults to ``None``, where no logo is displayed.

**logo_page** : `str` or `None`, `default="Home"`</br>
The page value that will be returned when the logo is selected, if there is
one. Defaults to ``"Home"``. For a non-clickable logo, set this to ``None``.

**urls** : `dict of str: str`, optional</br>
A dictionary with the page name as the key and an external URL as the value,
both as strings. The page name must be contained in the *pages* list. The URL
will open in a new window or tab. The default is ``None``.

**styles** : `dict of str: dict of str: str`, optional</br>
Apply CSS styles to desired targets, through a dictionary with the HTML tag or
pseudo-class name as the key and another dictionary to style it as the value.
In the second dictionary, the key-value pair is the name of a CSS property and
the value it takes. The keys and values must be strings. Defaults to ``None``,
where no custom style is applied.

The available HTML tags are: ``"nav"``, ``"div"``, ``"ul"``, ``"li"``, ``"a"``,
``"img"`` and ``"span"``. To better understand the document tree, check the
notes section.

The available pseudo-classes are: ``"active"`` and ``"hover"``, which direct
the styling to the ``"span"`` tag. The menu and sidebar buttons are only styled
by ``"hover"`` (if they are set to ``True`` in *adjust*). Currently,
``"hover"`` only accepts two CSS properties, they are: ``"color"`` and
``"background-color"``.

**adjust** : `bool` or `dict of str: bool` or `None`, `default=True`</br>
It makes a series of CSS adjustments and displays the navbar correctly, by
overriding some Streamlit behaviors.

It is possible to customize the adjustments with options that can be toggled on
or off. To do that, pass a dictionary with the option as the key and a boolean
as the value. The available options are: ``"show_menu"`` and
``"show_sidebar"``. To toggle all options to the same state, pass ``True``,
which is the parameter default value, or ``False`` to *adjust*. Note that it is
still needed to have ``st.sidebar`` in the app to be able to show the sidebar
button.

In most cases, the CSS adjustments do not interfere with the rest of the web
app, however there could be some situations where this occurs. If this happens,
or it is desired to disable all of them, pass ``None`` to *adjust* and, when
necessary, make your own CSS adjustments with ``st.markdown``.

**key** : `str` or `int`, optional</br>
A string or integer to use as a unique key for the component. If this is
omitted, a key will be generated for the widget based on its content. Multiple
navbars of the same type may not share the same key.

## Returns

**page** : `str` or `None`</br>
The page selected by the user. If there has been no interaction yet, returns
the preselected page or ``None``.

## Notes

### Theme variables
The component uses by default two CSS variables from the
[web app's theme](https://docs.streamlit.io/library/advanced-features/theming),
to style the ``"nav"`` tag. They are:

``` css
nav {
  font-family: var(--font);
  background-color: var(--primary-color);
}
```

It also accepts the theme variables to be passed in the *styles* dictionary, as
the values for the CSS properties, for example:

``` python
styles = {
    "span": {"color": "var(--text-color)"}
}
```

The theme variables that can be used are:

```
--primary-color
--background-color
--secondary-background-color
--text-color
--font
```

### Document tree

To style the navigation bar, it is important to understand its Document Object
Model (DOM), also known as document tree. Take a scenario where the navbar was
created with ``pages=["Hello, World!"]`` and an SVG logo. On the frontend side,
the component will build this DOM (simplified for readability):

```html
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
```

Notice that the ``"a"`` tag will style both the logo and the page name.
However, the ``"img"`` tag is unique to the logo, just as ``"span"`` is to the
pages names.

### Maximum width

A fundamental CSS property to adjust is the ``"max-width"`` for the ``"div"``
tag. That is because it controls how much space the page names will have
between them. The default value is ``"700px"``, which works well in most cases.
But if the navbar has a large number of pages, or longer names, it might be
necessary to increase the maximum width. Conversely, whenever the navbar has
few pages or short names, this value may need to be reduced.


## Examples

A basic example:
``` python
import streamlit as st
from streamlit_navigation_bar import st_navbar

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)
```
[![Example 1](https://github.com/gabrieltempass/streamlit-navigation-bar/raw/main/images/st_navbar_1.gif)](https://st-navbar-1.streamlit.app/)
[**[App]**](https://st-navbar-1.streamlit.app/) 
[**[Source]**](https://github.com/gabrieltempass/streamlit-navigation-bar/blob/main/examples/st_navbar_1/streamlit_app.py)

An example styling the navbar with a design similar to Streamlit's sidebar navigation:
``` python
import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "Library", "Tutorials", "Development", "Download"]
styles = {
	"nav": {
		"background-color": "rgb(240, 242, 246)",
	},
	"div": {
		"max-width": "31.25rem",
	},
	"span": {
		"color": "var(--text-color)",
		"border-radius": "0.5rem",
		"padding": "0.4375rem 0.625rem",
		"margin": "0 0.125rem",
	},
	"active": {
		"background-color": "rgba(151, 166, 195, 0.15)",
	},
	"hover": {
		"background-color": "rgba(151, 166, 195, 0.25)",
	},
}

page = st_navbar(pages, styles=styles)
st.write(page)

with st.sidebar:
	st.write("Sidebar")
```
[![Example 2](https://github.com/gabrieltempass/streamlit-navigation-bar/raw/main/images/st_navbar_2.gif)](https://st-navbar-2.streamlit.app/)
[**[App]**](https://st-navbar-2.streamlit.app/) 
[**[Source]**](https://github.com/gabrieltempass/streamlit-navigation-bar/blob/main/examples/st_navbar_2/streamlit_app.py)

An example using a logo, an external URL, multiple pages with content, among
other things:
``` python
import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Install", "User Guide", "API", "Examples", "Community", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "cubes.svg")
urls = {"GitHub": "https://github.com/gabrieltempass/streamlit-navigation-bar"}
styles = {
	"nav": {
		"background-color": "#7c18c4",
		"justify-content": "left",
	},
	"span": {
		"padding": "14px",
	},
	"active": {
		"background-color": "white",
		"color": "var(--text-color)",
		"font-weight": "normal",
		"padding": "14px",
	}
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    adjust=False,
)

functions = {
	"Home": pg.show_home,
	"Install": pg.show_install,
	"User Guide": pg.show_user_guide,
	"API": pg.show_api,
	"Examples": pg.show_examples,
	"Community": pg.show_community,
}
go_to = functions.get(page)
if go_to:
	go_to()
```
[![Example 3](https://github.com/gabrieltempass/streamlit-navigation-bar/raw/main/images/st_navbar_3.gif)](https://st-navbar-3.streamlit.app/)
[**[App]**](https://st-navbar-3.streamlit.app/) 
[**[Source]**](https://github.com/gabrieltempass/streamlit-navigation-bar/blob/main/examples/st_navbar_3/streamlit_app.py)

## Requirements

To use the navigation bar component in your Streamlit app, you will need:
* **Python 3.8+**
* **Streamlit 1.30+** (older versions of Streamlit will cause the *adjust*
parameter from ``st_navbar`` to not work properly when set to ``True`` or
``False``)

## Roadmap

The current version of the Streamlit Navigation Bar still has some limitations,
that are planned to be addressed in future updates. Those are:
* Be responsive on smaller screens.
* Accept ``.png`` and ``.jpg`` image formats for the logo.
* Style ``:link`` and ``:visited`` pseudo-classes and any CSS property for
``:hover``.
* Select predefined themes to style the navbar.
* Set light and dark mode styles for the navbar.
* Apply a format function to the displayed pages.

You are welcome to help develop these features and others. Below is a guide on
how to quickstart the development.

## Development

Ensure you have [Python 3.8+](https://www.python.org/downloads/),
[Node.js](https://nodejs.org) and
[npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
installed.

1. Clone this repository:
``` bash
git clone git@github.com:gabrieltempass/streamlit-navigation-bar.git
```

2. Go to the `frontend` directory and initialize and run the component template
frontend:
``` bash
cd streamlit-navigation-bar/streamlit_navigation_bar/frontend
```
``` bash
npm install
npm run dev
```

3. From a separate terminal, go to the repository root directory, create a new
Python virtual environment, activate it and install Streamlit,
[st-theme](https://github.com/gabrieltempass/streamlit-theme) and the template
as an editable package:
``` bash
cd streamlit-navigation-bar
```
``` bash
python3 -m venv venv
. venv/bin/activate
pip install streamlit
pip install st-theme
pip install -e .
```

Still from the same separate terminal, run the example Streamlit app:
``` bash
streamlit run streamlit_navigation_bar/example.py
```

If all goes well, you should see something like this:

![Quickstart success](https://github.com/gabrieltempass/streamlit-navigation-bar/raw/main/images/development.png)

Modify the frontend code at
`streamlit_navigation_bar/frontend/src/StNavbar.vue`.
Modify the Python code at `streamlit_navigation_bar/__init__.py`.

## References

This Streamlit component is based on:
* The [streamlit-component-vue-vite-template](https://github.com/gabrieltempass/streamlit-component-vue-vite-template)
repository, that uses Vue 3 to code the frontend and Vite to serve the files
locally during development, as well as bundle and compile them for production.
* The [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu/tree/master)
component, by [@victoryhb](https://github.com/victoryhb).
