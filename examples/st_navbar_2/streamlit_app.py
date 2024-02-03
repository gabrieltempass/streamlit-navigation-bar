import streamlit as st
from streamlit_navigation_bar import st_navbar

pages = ["Home", "Library", "Tutorials", "Development", "Download"]
styles = {
	"nav": {
	  "background-color": "#f0f2f6",
	  "height": "56px",
	},
	"span": {
		"color": "#45474d",
		"border": "solid",
		"border-width": "1px",
		"border-color": "#f0f2f6",
		"border-radius": "8px",
		"padding": "9px 12px",
		"margin": "0px 10x",
	},
	"selected": {
		"color": "white",
		"font-weight": "normal",
		"background-color": "#4285f4",
		"border": "solid",
		"border-width": "1px",
		"border-color": "#4285f4",
		"border-radius": "8px",
	},
}

page = st_navbar(pages, styles=styles)
st.write(page)
