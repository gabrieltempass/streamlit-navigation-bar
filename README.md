[![PyPI - Version](https://img.shields.io/pypi/v/streamlit-navigation-bar)](https://pypi.org/project/streamlit-navigation-bar/)
[![Downloads](https://static.pepy.tech/badge/streamlit-navigation-bar/month)](https://pepy.tech/project/streamlit-navigation-bar)
[![GitHub License](https://img.shields.io/github/license/gabrieltempass/streamlit-navigation-bar?color=blue)](https://github.com/gabrieltempass/streamlit-navigation-bar/blob/main/LICENSE)

# Streamlit Navigation Bar

**A component that allows you to place a navigation bar in your Streamlit app.**

The navbar was built to:
* Be simple to use
* Look great out of the box
* Apply custom styles
* Integrate with Streamlit’s UI
* Have a well-written documentation

It has some cool functionalities, like displaying an optional logo and external URLs. It also matches the active theme by default.

## Installation

Open a terminal and run:

``` bash
pip install streamlit-navigation-bar
```

## Example

Here is a basic example of how to use it:
``` python
import streamlit as st
from streamlit_navigation_bar import st_navbar

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)
```
[![Example 1](https://github.com/gabrieltempass/streamlit-navigation-bar/raw/main/images/st_navbar_1.gif)](https://st-navbar-1.streamlit.app/)
[**[App]**](https://st-navbar-1.streamlit.app/) 
[**[Source]**](https://github.com/gabrieltempass/streamlit-navigation-bar/blob/main/examples/st_navbar_1/streamlit_app.py)

Jump to the [examples gallery](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/Examples) to see more demos of what the navbar is capable of.

## Documentation

The complete documentation is on the [GitHub Wiki](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki).
There, you can check:
* [API reference](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference)
    * [Usage](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#usage)
    * [Parameters](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#parameters)
    * [Returns](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#returns)
    * [Styles](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#styles)
        * [Document Object Model](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#document-object-model)
        * [CSS variables](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#css-variables)
        * [Default style](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#default-style)
        * [Maximum width](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#maximum-width)
    * [Options](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/API-reference#options)
* [Multipage](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/Multipage)
    * [Streamlit's structure](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/Multipage#streamlits-structure)
    * [Recommended structure](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/Multipage#recommended-structure)
* [Examples](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/Examples)
* [Roadmap](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/Roadmap)

## Requirements

To use the navigation bar component in your Streamlit app, you will need:
* **Python >= 3.8**
* **Streamlit >= 1.33**
* **[Streamlit Theme](https://github.com/gabrieltempass/streamlit-theme) >= 1.2.3**
* The CSS adjustment depends on the
  [browser compatibility with the :has pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:has#browser_compatibility)

## Contributing

You are welcome to help develop the Streamlit Navigation Bar! There are
multiple ways to contribute, such as [reporting a bug](https://github.com/gabrieltempass/streamlit-navigation-bar/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml)
or [requesting a feature](https://github.com/gabrieltempass/streamlit-navigation-bar/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.yml).
You can also just [ask a question](https://github.com/gabrieltempass/streamlit-navigation-bar/issues/new?assignees=&labels=question&projects=&template=ask_question.yml),
or join the discussions in the [community forum](https://discuss.streamlit.io/t/new-component-streamlit-navigation-bar/66032).
To submit code for a pull request, make sure to read the
[guide on how to contribute](https://github.com/gabrieltempass/streamlit-navigation-bar/wiki/Contributing).

## References

The Streamlit Navigation Bar was made with:
* The [streamlit-component-vue-vite-template](https://github.com/gabrieltempass/streamlit-component-vue-vite-template),
  by [@gabrieltempass](https://github.com/gabrieltempass)
* The [st-theme](https://github.com/gabrieltempass/streamlit-theme)
  component, by [@gabrieltempass](https://github.com/gabrieltempass)

And based on:
* The [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu/tree/master)
  component, by [@victoryhb](https://github.com/victoryhb)
* The [styleable container](https://arnaudmiribel.github.io/streamlit-extras/extras/stylable_container/),
  by [@LukasMasuch](https://github.com/LukasMasuch)
