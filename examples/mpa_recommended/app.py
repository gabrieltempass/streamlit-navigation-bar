import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


st.set_page_config(initial_sidebar_state="collapsed")

styles = {"div": {"max-width": "350px"}}  # Reduce the page names spacing.
page = st_navbar(["Home", "Page 1", "Page 2"], styles=styles)

if page == "Home":
    pg.home()
elif page == "Page 1":
    pg.page_1()
elif page == "Page 2":
    pg.page_2()
