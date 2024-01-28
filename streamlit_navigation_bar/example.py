import streamlit as st

from streamlit_navigation_bar import st_navbar


pages = ["Sample Size", "Statistical Significance", "Theory", "About"]
page = st_navbar(pages, logo_svg="test")
st.write(page)
