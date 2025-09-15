import streamlit as st
import requests
#8501
# st.title("user management")

# @st.dialog("add user")
# def new_user():
#     course_id=-1
#     st.write("this is a form to creat user")
#     name=st.text_input("name",placeholder="enter the name")
#     username=st.text_input("username",placeholder="enter the username")
#     password=st.text_input("password",placeholder="enter the password",type="password")
#     course_id=st.selectbox("select course",["1.pet","2.cook"])
#     if course_id=="1.pet":
#         course_id=1
#     else:
#         course_id=2
#     st.button("submit",use_container_width=True, type="primary")
#     #api call and savein db
#     url=f"http://127.0.0.1:8000/users?name={name}&username{username}&password={password}&course_id={course_id}"
#     requests.post(url)
#     st.rerun()
# response=requests.get("http://127.0.0.1:8000/users")
# data=response.json()

# new_user_btn=st.button("new user +",type="primary")
# for user in data:
#     with  st.container(border=True):
#         st.subheader(user[1])#header subheader
#         st.caption("@"+user[2])
        
# if new_user_btn:
#     new_user()
# st.write(data)

st.title("User management")
response=requests.get( 'http://127.0.0.1:8000/users')
data=response.json()
for user in data:
    with st.container(border=True):
        st.write(user[1])
        st.caption("1"+user[2])
st.write(data)
 