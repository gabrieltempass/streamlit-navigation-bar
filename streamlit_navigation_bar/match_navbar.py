from streamlit.config import get_config_options
from streamlit_theme import st_theme


class MatchNavbar():
    configs = {
        "var(--primary-color)": "primaryColor",
        "var(--background-color)": "backgroundColor",
        "var(--secondary-background-color)": "secondaryBackgroundColor",
        "var(--text-color)": "textColor",
        "var(--font)": "font",
    }

    def __init__(self, styles, key):
        """
        styles : dict of str: dict of str: str
            Apply CSS styles to desired targets, through a dictionary with the
            HTML tag or pseudo-class name as the key and another dictionary to
            style it as the value. In the second dictionary, the key-value pair
            is the name of a CSS property and the value it takes. The keys and
            values must be strings.
        """
        self.styles = styles
        self.theme = st_theme(key=f"key_{key}")

    def _get_theme_config(self, theme_configs):
        """
        Get the value of a CSS property from the theme or a config option.

        Search for the value to style Streamlit's header and UI elements, e.g.
        menu and sidebar buttons, seamlessly with the navbar.

        It tries to first find it in the styles dictionary, then in the
        frontend theme object and finally in the configuration options. When it
        does not find with the first method, it goes to the next one in the
        sequence. Whenever the value is found it is returned immediately. If at
        the end it is still not found, returns a default value.

        When the function does not receive a name in `theme_config`, it does
        not go through the theme and configuration steps in the search
        sequence.

        Parameters
        ----------
        style : str or None
            The value of the CSS property, or the name of the theme variable
            and config option found in `styles`. Or ``None``, if nothing is
            found in `styles`.
        theme_config : str, optional
            The name of the frontend theme variable, and, at the same time,
            Streamlit's configuration option, to get the value from. The
            config option could be in a TOML file for example.
        default : str, optional
            The default value to be returned, in case the CSS property is not
            found in `styles`, `theme` or config options.

        Returns
        -------
        value : str
            The value of the CSS property found in `styles`, `theme`, config
            options or a default.
        """
        theme = self.theme
        configs = self.configs.values()

        # First, search for the theme variable and config option found in
        # `styles`. Then, do the same for the `theme_config` provided.
        for theme_config in theme_configs:

            # Return the CSS value from `theme`.
            if theme is not None and theme_config in theme:
                return theme[theme_config]

            # Return the CSS value from configs.
            if theme_config in configs:
                value = get_config_options()[f"theme.{theme_config}"].value
                if value is not None:
                    return value
        
        # Not found.
        return None

    def _get_style(self, css_property, targets):
        """
        Get the value of a CSS property from `styles`.

        Search for the value to style Streamlit's header and UI elements, e.g.
        menu and sidebar buttons, seamlessly with the navbar.

        It looks up for the CSS property in the styles dictionary, but only for
        given targets. When there is no `theme_config`, it will either return If a plain value is found, it is returned.



        If the value
        is a theme variable and config option, it transforms the name before
        returning it

        It tries to find with the first target,
            if it does not find it, it iterates to the next ones.

        It tries to first find it in the styles dictionary, then in the
        frontend theme object and finally in the configuration options. When it
        does not find with the first method, it goes to the next one in the
        sequence. Whenever the value is found it is returned immediately. If at
        the end it is still not found, returns a default value.

        When the function does not receive a name in `theme_config`, it does
        not go through the theme and configuration steps in the search
        sequence.

        Parameters
        ----------
        css_property : str
            The name of the CSS property to get the value from.
        targets : list of str
            A list with the targets (from the styles dictionary) where to look
            up the CSS property value. It tries to find with the first target,
            if it does not find it, it iterates to the next ones.

            The available HTML tags are: ``"nav"``, ``"div"``, ``"ul"``,
            ``"li"``, ``"a"``, ``"img"`` and ``"span"``. The available
            pseudo-classes are: ``"active"`` and ``"hover"``.
        theme_config : str, optional
            The name of the frontend theme variable, and, at the same time,
            Streamlit's configuration option, to get the value from. The
            config option could be in a TOML file for example.
        default : str, optional
            The default value to be returned, in case the CSS property is not
            found in `styles`, and there is no need to search in `theme` or
            configs.

        Returns
        -------
        value : str or None
            If `theme_config` is ``None``, returns the value of the CSS
            property found in `styles`, or a default. Else, the value of the
            CSS property or the name of the theme variable and config option
            found in `styles`, or ``None``.
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

        When the function does not receive a name in `theme_config`, it does
        not go through the theme and configuration steps in the search
        sequence.

        Parameters
        ----------
        css_property : str
            The name of the CSS property to get the value from.
        targets : list of str
            A list with the targets (from the styles dictionary) where to look
            up the CSS property value. It tries to find with the first target,
            if it does not find it, it iterates to the next ones.

            The available HTML tags are: ``"nav"``, ``"div"``, ``"ul"``,
            ``"li"``, ``"a"``, ``"img"`` and ``"span"``. The available
            pseudo-classes are: ``"active"`` and ``"hover"``.
        theme_config : str, optional
            The name of the frontend theme variable, and, at the same time,
            Streamlit's configuration option, to get the value from. The
            config option could be in a TOML file for example.
        default : str, optional
            The default value to be returned, in case the CSS property is not
            found in `styles`, `theme` or config options.

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
