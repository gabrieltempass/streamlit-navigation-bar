import streamlit as st
from streamlit_navigation_bar import st_navbar


st.set_page_config(initial_sidebar_state="collapsed")

styles = {"div": {"max-width": "350px"}}  # Reduce the page names spacing.
page = st_navbar(["Home", "Page 1", "Page 2"], selected="Page 2", styles=styles)

if page == "Home":
    st.switch_page("home.py")
if page == "Page 1":
    st.switch_page("pages/page_1.py")

# Page 2 content goes here, for example:
st.write("Baz")
