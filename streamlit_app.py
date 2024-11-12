import streamlit as st
import numpy as np

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        #st.session_state.pw=st.number_input('Please input password:',value=None)
        st.session_state.logged_in = True
        st.rerun()
        
def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()
 
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
story2_page = st.Page('pages/page_2.py', title="story2", icon=":material/home:")
story3_page = st.Page("pages/page_3.py", title="story3", icon=":material/key:")
story4_page = st.Page("pages/page_4.py", title="story4", icon=":material/key:")
story5_page = st.Page("pages/page_5.py", title="story5", icon=":material/key:")
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.title("🎈 My taipei story")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
st.write(    "Let's test again!")
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Storys": [story2_page,story3_page,story4_page,story5_page],
            
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()

