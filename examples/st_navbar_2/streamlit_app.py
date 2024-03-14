import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "Library", "Tutorials", "Development", "Download"]
styles = {
	"div": {
		"max-width": "32rem",
	},
	"span": {
		"border-radius": "0.5rem",
		"padding": "0.4375rem 0.625rem",
		"margin": "0 0.125rem",
	},
	"active": {
		"background-color": "rgba(151, 166, 195, 0.15)",
	},
	"hover": {
		"background-color": "rgba(151, 166, 195, 0.25)",
	},
}

page = st_navbar(pages, styles=styles)
st.write(page)

with st.sidebar:
	st.write("Sidebar")
