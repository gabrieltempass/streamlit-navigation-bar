import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg


st.set_page_config(
    page_title="Streamlit Navigation Bar Example 3",
    initial_sidebar_state="collapsed",
)

pages = ["Install", "User Guide", "API", "Examples", "Community", "GitHub"]
urls = {"GitHub": "https://github.com/gabrieltempass/streamlit-navigation-bar"}
styles = {
	"nav": {
		"background-color": "#7c18c4",
		"justify-content": "left",
	},
	"span": {
		"padding": "14px",
	},
	"selected": {
		"background-color": "white",
		"color": "var(--text-color)",
		"font-weight": "normal",
		"padding": "14px",
	},
}

page = st_navbar(
    pages,
    selected="Home",
    logo_path="cubes.svg",
    urls=urls,
    styles=styles,
)

if page == "Home":
	pg.show_home()
elif page == "Install":
	pg.show_install()
elif page == "User Guide":
	pg.show_user_guide()
elif page == "API":
	pg.show_api()
elif page == "Examples":
	pg.show_examples()
elif page == "Community":
	pg.show_community()

html = {
    "hide_sidebar_button": """
        <style>
            div[data-testid="collapsedControl"] {
                visibility: hidden;
            }
        </style>
    """,
}

st.markdown(html["hide_sidebar_button"], unsafe_allow_html=True)
