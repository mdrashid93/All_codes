import streamlit as st
from supabase import create_client
data=create_client("")

tabs=st.tabs(['login','signup'])
 


with tabs[0]:
    email=st.text_input('username',placeholder='placeholder')
    pasword=st.text_input('password',placeholder='password')
    signup=st.button('login',type='primary',use_container_width=True)
    if signup_btn:
        response = supabase.auth.sign_up({
        "email": email,
        "password": password
         }
        )
        st.write(response.user)
        
with tabs[1]:
    username=st.text_input('username',placeholder='placeholder')
    password=st.text_input('password',placeholder='password',type='password' )
    login=st.button('login',type='primary',use_container_width=True)
    if login_btn:
       # database.auth.sign_in_with_password 
        res=response = supabase.auth.sign_up({
        "email": email,
        "password": password
         }
        )
        st.write(res.session.access_token)
        pg=st.navigation([st.page("home.py"),st.page("page_2.py")])