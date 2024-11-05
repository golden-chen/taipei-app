import streamlit as st
import numpy as np

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.pw=st.number_input('Please input password:',value=None)
        st.write("The current number is ", st.session_state.pw)       
        pw1=st.number_input('Please wait!',value=None)
        if st.session_state.pw=='1234.00':
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.write('password is wrong!')
def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
story2_page = st.Page('pages/page_2.py', title="story2", icon=":material/home:")
story3_page = st.Page("pages/page_3.py", title="story3", icon=":material/key:")
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.title("🎈 My taipei story")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
st.write(    "Let's test again!")
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Storys": [story2_page,story3_page],
            
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()

