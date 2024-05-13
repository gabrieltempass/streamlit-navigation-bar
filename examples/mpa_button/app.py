import streamlit as st
from streamlit import session_state as ss
from streamlit_navigation_bar import st_navbar

import pages as pg


# If running locally, follow these steps after the app initializes or
# refreshes:
#   1. Clear the cache, either through the menu option or by pressing C.
#   2. Rerun the app, either through the menu option or by pressing R.
# This will ensure the `selected` variable is properly set to "Home".

st.set_page_config(initial_sidebar_state="collapsed")

selected = "Home" if "selected" not in ss else ss["selected"]
styles = {"div": {"max-width": "350px"}}  # Reduce the page names spacing.
page = st_navbar(
    pages=["Home", "Page 1", "Page 2"],
    selected=selected,
    styles=styles,
    key="selected",
)

if page == "Home":
    pg.home()
elif page == "Page 1":
    pg.page_1()
elif page == "Page 2":
    pg.page_2()
