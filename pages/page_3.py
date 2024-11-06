import streamlit as st
import foo
import time
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
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
 
    def set_state(i):
        st.session_state.stage = i
    
    if st.session_state.stage == 0:
        cols[1].button('Begin', on_click=set_state, args=[1])
    
    if st.session_state.stage >= 1:
        name = cols[1].text_input('Name', on_change=set_state, args=[2])
    
    if st.session_state.stage >= 2:
        cols[1].write(f'Hello {name}!')
        color = cols[1].selectbox(
            'Pick a Color',
            [None, 'red', 'orange', 'green', 'blue', 'violet'],
            on_change=set_state, args=[3]
        )
        if color is None:
            set_state(2)

    if st.session_state.stage >= 3:
        cols[1].write(f':{color}[Thank you!]')
        cols[1].button('Start Over', on_click=set_state, args=[0])
with tab3:
    cols=st.columns(2)
    cols[0].header("An owl")
    cols[0].image("https://static.streamlit.io/examples/owl.jpg", width=100)
    with st.spinner('Wait for it...'):
        time.sleep(5)
    cols[1].success("Done!")
