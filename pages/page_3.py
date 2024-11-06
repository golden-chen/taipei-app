import streamlit as st
import foo
import time
import pandas as pd
st.write(foo.hello)
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
tab1, tab2, tab3 ,tab4,tab5= st.tabs(["Cat", "Dog", "Owl","frame","container"])

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
    cols[1].success("Done!", icon="✅")
with tab4:
    def expensive_process(option, add):
        with st.spinner('Processing...'):
            time.sleep(5)
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C':[7, 8, 9]}) + add
        return (df, add)

    cols = st.columns(2)
    option = cols[0].selectbox('Select a number', options=['1', '2', '3'])
    add = cols[1].number_input('Add a number', min_value=0, max_value=10)
    
    if 'processed' not in st.session_state:
        st.session_state.processed = {}
    
    # Process and save results
    if st.button('Process'):
        result = expensive_process(option, add)
        st.session_state.processed[option] = result
    
    if option in st.session_state.processed:
        st.write(f'Option {option} processed with add {add}')
        st.write(st.session_state.processed[option][0])
with tab5:
    row1 = st.columns(2)
    row2 = st.columns(2)
    
    for col in row1 + row2:
        tile = col.container(height=130)
        tile.title(":balloon:")
        with tile:
            if st.button('Button-1'):
                st.write('Button 1 was clicked')
                if st.button('Button-2'):
                    # This will never be executed.
                    st.write('Button 2 was clicked')
