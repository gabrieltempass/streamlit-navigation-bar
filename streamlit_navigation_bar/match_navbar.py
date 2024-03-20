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
        self.styles = styles
        self.theme = st_theme(key=f"key_{key}")

    def _get_theme_config(self, style, option, default):
        configs = self.configs.values()
        theme = self.theme
        value = None

        # Return value found in `_get_style()`.
        if style is not None and style not in configs:
            return style

        # Search first for the style theme variable value, if there is one.
        # Then, do the same for the option provided.
        searches = [option]
        if style is not None:
            searches.insert(0, style)
        for search in searches:

            # Get the CSS value from `theme`.
            if theme is not None and search in theme:
                return theme[search]

            # Get the CSS value from configs.
            if search in configs:
                value = get_config_options()[f"theme.{search}"].value
                if value is not None:
                    return value
        
        # Return the default.
        if value is None:
            return default

    def _get_style(self, targets, css_property, option=None, default=None):
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
        # Search for the CSS value in `styles`.
        styles = self.styles
        configs = self.configs

        if styles is not None:
            for target in targets:
                if target in styles and css_property in styles[target]:
                    style = styles[target][css_property]

                    # Return a plain value.
                    if style not in configs:
                        return style

                    # Return `var(--theme-variable)` transformed to `themeVariable`.
                    return configs[style]

        # No need to search in `theme` or configs.
        if option is None:
            return default

        # Will be searched in `theme` and configs later.
        return None

    def get_value(self, targets, css_property, option=None, default=None):
        if option is None:
            return self._get_style(targets, css_property, default=default)

        style = self._get_style(targets, css_property)
        return self._get_theme_config(style, option, default)
