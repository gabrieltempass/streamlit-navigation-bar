import os

import streamlit as st

from streamlit_navigation_bar import st_navbar


st.set_page_config(
    page_title="Streamlit Navigation Bar",
    initial_sidebar_state="collapsed",
)

pages = ["Documentation", "Examples", "Community", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "logo.svg")
urls = {"GitHub": "https://github.com"}
styles = {"nav": {"background-color": "black"}}

page = st_navbar(
    pages,
    selected="Home",
    logo_path=logo_path,
    urls=urls,
    styles=styles
)

st.write(page)
