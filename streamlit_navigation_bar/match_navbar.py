from streamlit.config import get_config_options
from streamlit_theme import st_theme


class MatchNavbar():
    """
    Represent a user interface object with a style that matches the navbar.

    Attributes
    ----------
    configs : dict of {str : str}
        A dictionary that maps CSS variables to theme variables names, which
        are also config options.
    styles : dict of {str : dict of {str : str}}
        A dictionary with the HTML tag or pseudo-class name as the key and
        another dictionary to style it as the value. In the second dictionary,
        the key-value pair is the name of a CSS property and the value it
        takes, both in string format. It accepts CSS variables to be passed as
        values.
    key : str, int or None
        A key associated with the container that gets the theme. This needs to
        be unique since all styles will be applied to the container with this
        key.

    Methods
    -------
    get_value(css_property, targets, default, theme_config=None)
        Get the value of a CSS property.
    """

    configs = {
        "var(--primary-color)": "primaryColor",
        "var(--background-color)": "backgroundColor",
        "var(--secondary-background-color)": "secondaryBackgroundColor",
        "var(--text-color)": "textColor",
        "var(--font)": "font",
    }

    def __init__(self, styles, key):
        """
        Instantiate a user interface object to get CSS that matches the navbar.

        Parameters
        ----------
        styles : dict of {str : dict of {str : str}}
            A dictionary with the HTML tag or pseudo-class name as the key and
            another dictionary to style it as the value. In the second
            dictionary, the key-value pair is the name of a CSS property and
            the value it takes, both in string format. It accepts CSS variables
            to be passed as values.
        key : str, int or None
            A key associated with the container that gets the theme. This needs
            to be unique since all styles will be applied to the container with
            this key.
        """
        self.styles = styles
        self.theme = st_theme(key=f"key_{key}")

    def _get_theme_config(self, theme_configs):
        """
        Get the value of a CSS property from the theme or config option.

        Try to find the value with the name at the beginning of the list.
        Search first in the frontend theme object and then in the configuration
        options. In case it does not find it, iterates to the next name.
        Whenever the value is found it is returned immediately. If at the end
        it is still not found, returns ``None``.

        Parameters
        ----------
        theme_configs : list of str
            A list with the names of the frontend theme variables, which are
            also Streamlit's configuration options, to get the value from.

        Returns
        -------
        value : str or None
            The value of the CSS property found in `styles`, `theme` or config
            options. If not found, returns ``None``.
        """
        theme = self.theme
        configs = self.configs.values()

        # Get the value for the var in `styles`, then, for the `theme_config`.
        for theme_config in theme_configs:

            # Return the CSS value from `theme`.
            if theme is not None and theme_config in theme:
                return theme[theme_config]

            # Return the CSS value from configs, like a TOML file.
            if theme_config in configs:
                value = get_config_options()[f"theme.{theme_config}"].value
                if value is not None:
                    return value
        
        # Not found.
        return None

    def _get_style(self, css_property, targets):
        """
        Get the value of a CSS property from a styles dictionary.

        Try to find the value with the target at the beginning of the list. In
        case it does not find it, iterates to the next target. Whenever the
        value is found it is returned immediately. If at the end it is still
        not found, returns ``None``.

        The value found and returned will be either a plain CSS value, or the
        name of a theme variable and config option, which the
        `_get_theme_config` function will get its value later.

        Parameters
        ----------
        css_property : str
            The name of the CSS property to get the value from.
        targets : list of str
            A list with the targets where to look up the CSS property value in
            the styles dictionary. It tries to find with the first target,
            if it does not find it, it iterates to the next ones.

            The available targets are: ``"nav"``, ``"div"``, ``"ul"``,
            ``"li"``, ``"a"``, ``"img"``, ``"span"``, ``"active"`` and
            ``"hover"``.

        Returns
        -------
        value : str or None
            The value of the CSS property or the name of the theme variable and
            config option, found in `styles`. If not found, returns ``None``.
        """
        styles = self.styles
        configs = self.configs

        # Search for the CSS value in `styles`.
        for target in targets:
            if target in styles and css_property in styles[target]:
                value = styles[target][css_property]

                # Return a plain value.
                if value not in configs:
                    return value

                # Return `var(--theme-variable)` changed to `themeVariable`.
                return configs[value]

        # Not found.
        return None

    def get_value(self, css_property, targets, default, theme_config=None):
        """
        Get the value of a CSS property.

        Search for the value to style Streamlit's header and UI elements, e.g.
        menu and sidebar buttons, seamlessly with the navbar.

        It tries to first find it in the styles dictionary, then in the
        frontend theme object and finally in the configuration options. When it
        does not find with the first method, it goes to the next one in the
        sequence. Whenever the value is found it is returned immediately. If at
        the end it is still not found, returns a default value.

        Parameters
        ----------
        css_property : str
            The name of the CSS property to get the value from.
        targets : list of str
            A list with the targets where to look up the CSS property value in
            the styles dictionary. It tries to find with the first target, if
            it does not find it, it iterates to the next ones.

            The available targets are: ``"nav"``, ``"div"``, ``"ul"``,
            ``"li"``, ``"a"``, ``"img"``, ``"span"``, ``"active"`` and
            ``"hover"``.
        default : str
            The default value to be returned, in case the CSS property is not
            found in `styles`, `theme` or config options.
        theme_config : str, optional
            The name of the frontend theme variable, which is also Streamlit's
            configuration option, to get the value from. Defauls to ``None``,
            where the function does not go through the theme and configuration
            steps in the search sequence.

        Returns
        -------
        value : str
            The value of the CSS property found in `styles`, `theme`, config
            options or a default.
        """
        configs = self.configs.values()
        value = None
        theme_configs = []

        if self.styles is not None:
            value = self._get_style(css_property, targets)

        # Return plain value found in `styles`.
        if value is not None and value not in configs:
            return value

        # Not found in `styles` and no need to search in `theme` or configs.
        if value is None and theme_config is None:
            return default

        # Theme variable and config option found in `styles`.
        if value in configs:
            theme_configs.append(value)

        theme_configs.append(theme_config)
        value = self._get_theme_config(theme_configs)

        # Not found, return the default.
        if value is None:
            return default

        return value
