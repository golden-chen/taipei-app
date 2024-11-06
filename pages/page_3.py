import streamlit as st
import foo
st.write(foo.hello)
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    cols=st.columns(2)
    cols[0].header("A cat")
    cols[0].image("https://static.streamlit.io/examples/cat.jpg", width=100)
    if 'button' not in st.session_state:
        st.session_state.button = False
 
    def click_button():
        st.session_state.button = not st.session_state.button
    
    cols[1].button('Click me', on_click=click_button)
    
    if st.session_state.button:
        # The message and nested widget will remain on the page
        cols[1].write('Button is on!')
        cols[1].slider('Select a value')
    else:
        cols[1].write('Button is off!')
    cols[1].divider()
    cols[1].slider('Set a value', disabled=not st.session_state.button)

with tab2:
    cols=st.columns(2)
    cols[0].header("A dog")
    cols[0].image("https://static.streamlit.io/examples/dog.jpg", width=100)
with tab3:
    cols=st.columns(2)
    cols[0].header("An owl")
    cols[0].image("https://static.streamlit.io/examples/owl.jpg", width=100)
