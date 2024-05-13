import streamlit as st


def handle_click(page):
    st.session_state["selected"] = page


def home():
    # Home content goes here, for example:
    st.write("Foo")
    st.button("Go to Page 1", on_click=handle_click, args=["Page 1"])
    st.button("Go to Page 2", on_click=handle_click, args=["Page 2"])
