from streamlit.errors import StreamlitAPIException


def _type_error(param, name, expected):
    """Format a string with markdown syntax to describe a type error."""
    format_exp = ""
    first = True
    for exp in expected:
        if first:
            first = False
        else:
            format_exp += " or "
        format_exp += f"*{exp}*"

    return (
        f"The {name} parameter from st_navbar() received an invalid type.\n"
        f"\nExpected: {format_exp}  "
        f"\nGot: *{type(param).__name__}*"
    )


def _dict_error(param, name, case, value_expected):
    """Format a string with markdown syntax to describe a dictionary error."""
    if case == "key":
        got = f"{type(param).__name__}: {value_expected}"
    elif case == "value":
        got = f"str: {type(param).__name__}"

    return (
        f"The {name} parameter from st_navbar() received a dictionary that "
        f"has a {case} with an invalid type.\n"
        f"\nExpected: *dict of str: {value_expected}*  "
        f"\nGot: *dict of {got}*"
    )


def check_pages(pages):
    """Check if `pages` has a valid type and the minimum length required."""
    if not isinstance(pages, list):
        raise StreamlitAPIException(_type_error(pages, "pages", ["list"]))

    if not len(pages) > 0:
        raise StreamlitAPIException(
            "The pages parameter from st_navbar() received a list with an "
            "invalid length. The length must be larger than or equal to one.\n"
            "\nExpected: *len*(pages) >= 1  "
            f"\nGot: *len*(pages) == {len(pages)}"
        )

    for page in pages:
        if not isinstance(page, str):
            i = pages.index(page)
            raise StreamlitAPIException(
                "The pages parameter from st_navbar() received a list that "
                "has an item with an invalid type.\n"
                f"\nExpected: *type*(pages[{i}]) == *str*  "
                f"\nGot: *type*(pages[{i}]) == *{type(page).__name__}*"
            )


def check_selected(selected, logo_page, logo_path, pages):
    """Check if `selected` has a valid type and value."""
    sentinel = object()
    if selected is None or type(selected) == object:
        return

    if not isinstance(selected, str):
        raise StreamlitAPIException(
            _type_error(selected, "selected", ["str", "None"])
        )

    if selected not in pages:
        if selected != logo_page:
            raise StreamlitAPIException(
                "The selected parameter from st_navbar() received an invalid "
                "value. The value must be contained in the pages parameter list "
                "or be equal to the logo_page (if there is a logo).\n"
                f"\nExpected: selected in pages or selected == logo_page  "
                f"\nGot: '{selected}' not in {pages} and '{selected}' != "
                f"'{logo_page}'"
            )

        if selected == logo_page and logo_path is None:
            raise StreamlitAPIException(
                "The selected parameter from st_navbar() received an invalid "
                "value. If the value is not contained in the pages parameter "
                "list, and it is equal to the logo_page, it must have a valid "
                "logo_path that is different than None."
            )


def check_logo_path(logo_path):
    """Check if `logo_path` has a valid type."""
    if not isinstance(logo_path, str) and logo_path is not None:
        raise StreamlitAPIException(
            _type_error(logo_path, "logo_path", ["str", "None"])
        )


def check_logo_page(logo_page):
    """Check if `logo_page` has a valid type."""
    if not isinstance(logo_page, str) and logo_page is not None:
        raise StreamlitAPIException(
            _type_error(logo_page, "logo_page", ["str", "None"])
        )


def check_urls(urls, pages):
    """Check if `urls` has types and pages that are valid."""
    if urls is None:
        return

    if not isinstance(urls, dict):
        raise StreamlitAPIException(
            _type_error(urls, "urls", ["dict", "None"])
        )

    if len(urls) > len(pages):
        raise StreamlitAPIException(
            "The urls parameter from st_navbar() received a dictionary with "
            "an invalid length. The length must be smaller than or equal to "
            "the list length of the pages parameter.\n"
            f"\nExpected: *len*(urls) <= {len(pages)}  "
            f"\nGot: *len*(urls) = {len(urls)}"
        )

    for page, url in urls.items():
        if not isinstance(page, str):
            raise StreamlitAPIException(
                _dict_error(page, "urls", "key", "str")
            )

        if page not in pages:
            raise StreamlitAPIException(
                "The urls parameter from st_navbar() received a dictionary "
                "that has an invalid key. The key must be contained in the "
                "pages parameter list.\n"
                f"\nExpected: urls key in pages  "
                f"\nGot: '{page}' not in {pages}"
            )

        if not isinstance(url, str):
            raise StreamlitAPIException(
                _dict_error(url, "urls", "value", "str")
            )


def check_styles(styles):
    """Check if `styles` has types and targets that are valid."""
    if styles is None:
        return

    if not isinstance(styles, dict):
        raise StreamlitAPIException(
            _type_error(styles, "styles", ["dict", "None"])
        )

    for target, style in styles.items():
        if not isinstance(target, str):
            raise StreamlitAPIException(
                _dict_error(target, "styles", "key", "dict")
            )

        targets = [
            "nav", "div", "ul", "li", "a", "img", "span", "active", "hover"
        ]
        if target not in targets:
            raise StreamlitAPIException(
                "The styles parameter from st_navbar() received a dictionary "
                "that has an invalid key. The key must be one of the "
                "available HTML tags or pseudo-classes.\n"
                f"\nExpected: 'nav', 'div', 'ul', 'li', 'a', 'img', 'span', "
                "'active', 'hover'  "
                f"\nGot: '{target}'"
            )

        if not isinstance(style, dict):
            raise StreamlitAPIException(
                _dict_error(style, "styles", "value", "dict")
            )

        for css_property, value in style.items():
            if not isinstance(css_property, str):
                raise StreamlitAPIException(
                    _dict_error(css_property, "styles", "key", "str")
                )

            if not isinstance(value, str):
                raise StreamlitAPIException(
                    _dict_error(value, "styles", "value", "str")
                )


def check_options(options):
    """Check if `options` has types, keys and values that are valid."""
    if isinstance(options, bool):
        return

    if not isinstance(options, dict):
        raise StreamlitAPIException(
            _type_error(options, "options", ["bool", "dict"])
        )

    for option, toggle in options.items():
        if not isinstance(option, str):
            raise StreamlitAPIException(
                _dict_error(option, "options", "key", "bool")
            )

        available = [
            "show_menu",
            "show_sidebar",
            "hide_nav",
            "fix_shadow",
            "use_padding",
        ]
        if option not in available:
            raise StreamlitAPIException(
                "The option parameter from st_navbar() received a dictionary "
                "that has an invalid key. The key must be the name of one of "
                "the available options.\n"
                f"\nExpected: 'show_menu', 'show_sidebar', 'hide_nav', "
                "'fix_shadow', 'use_padding'  "
                f"\nGot: '{option}'"
            )

        if not isinstance(toggle, bool):
            raise StreamlitAPIException(
                _dict_error(toggle, "options", "value", "bool")
            )


def check_adjust(adjust):
    """Check if `adjust` has a valid type."""
    if not isinstance(adjust, bool):
        raise StreamlitAPIException(
            _type_error(adjust, "adjust", ["bool"])
        )


def check_key(key):
    """Check if `key` has a valid type."""
    if not isinstance(key, str) and not isinstance(key, int) and key is not None:
        raise StreamlitAPIException(
            _type_error(key, "key", ["str", "int", "None"])
        )
