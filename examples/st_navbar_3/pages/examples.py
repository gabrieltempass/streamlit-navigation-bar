import streamlit as st


def show_examples():
    st.header("Examples")
    col_1, col_2 = st.columns(2, gap="medium")
    col_1.write(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vel augue 
        nec tellus pulvinar blandit at nec lacus. Fusce eu libero quis nisi vehicula 
        ornare. Integer cursus quam suscipit tempor iaculis. Mauris vitae accumsan 
        felis, at elementum urna. Aenean in urna ante. Etiam ac dignissim dolor. 
        Aliquam convallis pretium mauris, vel imperdiet quam fringilla vitae. Donec ac 
        nisi eget nulla cursus consectetur a vitae purus. Quisque vitae aliquet ipsum, 
        quis venenatis odio. Quisque mauris elit, elementum et eros et, varius 
        efficitur magna. Proin dictum tristique tellus, quis viverra lorem tempor 
        vitae. Nulla quis bibendum libero, quis malesuada nisi. Mauris vel aliquam 
        odio. Maecenas nec tortor consectetur, posuere elit vel, sodales ante. Sed ut 
        pretium massa, ut dictum nibh.
        """
    )
    col_2.write(
        """
        Etiam dolor sem, bibendum id lacus eget, porta hendrerit mauris. Fusce varius 
        consequat erat, sit amet rhoncus lectus vestibulum vel. Cras vitae lacinia 
        nibh. Aenean varius facilisis tellus, vitae egestas magna pharetra ut. Maecenas 
        condimentum metus diam, facilisis rhoncus lorem lacinia eu. Maecenas eleifend 
        mauris velit, vitae placerat elit commodo ut. Ut ut purus elit. Suspendisse 
        condimentum quam sit amet vulputate vehicula. Nulla et quam at mauris cursus 
        euismod. Curabitur nec massa non tortor commodo condimentum eu at metus. Fusce 
        aliquet dolor nulla, quis feugiat sem bibendum vel. Donec tempus placerat leo 
        vitae blandit.
        """
    )
