import streamlit as st
import foo
st.write(foo.hello)
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    cols=st.columns(2)
    cols[0].image("https://static.streamlit.io/examples/cat.jpg", width=100)
    if 'button' not in st.session_state:
        st.session_state.button = False
 
    def click_button():
        st.session_state.button = not st.session_state.button
    
    st.button('Click me', on_click=click_button)
    
    if st.session_state.button:
        # The message and nested widget will remain on the page
        st.write('Button is on!')
        st.slider('Select a value')
    else:
        st.write('Button is off!')
    st.divider()
    st.slider('Set a value', disabled=not st.session_state.button)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=100)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=100)
