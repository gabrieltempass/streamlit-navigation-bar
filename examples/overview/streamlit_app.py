import streamlit as st
from streamlit_navigation_bar import st_navbar


st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "Install", "Documentation", "Examples", "GitHub"]
urls = {"GitHub": "https://github.com/gabrieltempass/streamlit-navigation-bar"}
styles = {"div": {"max-width": "35rem"}}

page = st_navbar(pages, urls=urls, styles=styles)

st.header(page)

if page == "Home":
    st.write(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at aliquam
        tortor, eget cursus purus. Vestibulum porta eget lacus ut tempus.
        Suspendisse mollis ex quis erat ullamcorper, sit amet mollis mi varius.
        Ut a consectetur dolor, non laoreet erat. Donec convallis vel lorem non
        lobortis. Cras lobortis, dolor ac rutrum ornare, lacus massa dapibus
        justo, et viverra lectus augue non purus. Morbi tincidunt lacinia
        turpis, et elementum mi pellentesque porttitor. Cras blandit lectus
        massa, ac sollicitudin urna mollis eu.

        Nunc vestibulum fringilla ipsum ac fringilla. Suspendisse eget lectus
        at augue cursus maximus. Nullam vel nibh quis ex fermentum laoreet.
        Maecenas nec suscipit neque. Fusce ac dictum dolor, eu pharetra nisi.
        Nunc nec augue at velit dignissim viverra. Quisque convallis in ante
        non placerat. Mauris dolor leo, dictum eu laoreet eleifend, molestie at
        dolor. Phasellus rutrum urna id semper ornare.

        Donec sagittis rhoncus dictum. Praesent sed lobortis lorem, sed
        venenatis tellus. Sed nunc sapien, pharetra vitae luctus in, posuere
        euismod quam. Sed dapibus nibh et aliquet fringilla. Phasellus a
        bibendum elit. Mauris tincidunt semper lacus eget mollis. Sed dapibus
        leo ut augue cursus, ac elementum ex ultricies. Ut nisl diam, tincidunt
        nec lectus vel, egestas mattis ligula. Morbi finibus fermentum varius.
        Mauris laoreet commodo lacus et tempor. Donec id nisl pharetra felis
        tempor porttitor. Fusce porta libero ut dui porta suscipit.
        """
    )
elif page == "Install":
    st.write(
        """
        Mauris neque dui, scelerisque vel consequat maximus, hendrerit nec
        lorem. Vestibulum suscipit tortor nec gravida imperdiet. Morbi eget ex
        sed nunc hendrerit bibendum in ultrices urna. Pellentesque vitae est
        tellus. Maecenas fringilla ullamcorper tempus. Nulla molestie arcu
        quam. In et nibh a enim volutpat molestie ac id metus.
        """
    )
elif page == "Documentation":
    st.write(
        """
        Maecenas mollis, mauris sit amet pretium convallis, massa augue
        scelerisque felis, in sagittis ante risus quis arcu. Nullam eu dolor id
        tellus venenatis dapibus. Praesent a feugiat metus, a congue leo.
        Suspendisse ipsum nunc, mattis eget luctus vel, molestie in ante.
        Aliquam erat volutpat. Donec sollicitudin quam ac aliquet pellentesque.
        """
    )
elif page == "Examples":
    st.write(
        """
        Sed egestas justo vel leo pulvinar fringilla. Nam aliquam metus vitae
        odio aliquam, in laoreet sapien tempus. Sed sit amet mauris quam.
        Curabitur euismod convallis sapien, sed euismod tellus finibus ac.
        Mauris ut felis vehicula, tincidunt magna quis, dignissim nisi. In
        neque nisi, ultricies in lobortis at, venenatis non neque.
        """
    )

with st.sidebar:
    st.header("Sidebar")
