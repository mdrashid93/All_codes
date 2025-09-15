#one------------------------------------------------------

# st.title("hello world ")
# st.subheader("bro how are you ")
# st.text("stremlit ")
# st.write("choose ")

# chai=st.selectbox("your faveroute chai:",["masala","lemon","adrak","ginger","orange "])
# st.write(f"your choice{chai}. excellent choice")
# st.success("your chai has brewed")


#two-------------------------------------------------------


# st.title("chai maker app")
# if st.button("make chai"):
#     st.success("your chai is being brewed")

# add_masala=st.checkbox("add masala")
# if add_masala:
#     st.write("masala added to your chai")
    
# tea_type=st.radio("pick your chai",["milk","water","almond",])
# st.write(f"selected base;{tea_type}")

# flavour=st.selectbox("choose flvour",["adrak","kesar","tulsi"])
# st.write(f"selected base{flavour}")

# sugar=st.slider("sugar level",0,5,2)
# st.write(f"selected sugar level{sugar}")

# cups=st.number_input("how many cups",min_value=1,max_value=10,step=1)
# st.write(f"selected sugar level {cups}")

# name=st.text_input("enter your name")
# if name:
#     st.write(f"welcome, {name}your chai is on the way")

# dob=st.date_input("selct your dob")
# st.write(f"your dob is,{dob}")



#three-------------------------------------------------
# st.title("chai taste poll")

# col1,col2=st.columns(2)
# with col1:
#     st.header("masala chai")
#     st.image("https://media.istockphoto.com/id/2159379151/photo/four-cup-of-tea-on-plate-friends-sharing-happiness-together-to-drink-and-relax.jpg?s=1024x1024&w=is&k=20&c=xudZJwYy_VjuK-ctbZuRCCRE_cDA36yjqleO5aiaEEk=",width=200)
#     vote1=st.button("vote masala chai")
# with col2:
#     st.header("adrak chai")
#     st.image("https://images.pexels.com/photos/1583582/pexels-photo-1583582.jpeg" ,width=200)
#     vote2=st.button("vote adrak chai")

# if vote1:
#     st.success("thanks for voting masala chai")
# elif vote2:
#     st.success("thanks for voting adrak chai")
    
# name=st.sidebar.text_input("enter your name")
# tea=st.sidebar.selectbox("choose your chai",["masala","kesar","adrak"])
# st.write(f"welcome {name} and your {tea} getting ready")


# with st.expander("show chai making instructions"):
#     st.write("""
#     1.boil water with tea leaves
#     2.add milk and spices
#     3.serve hot
#              """)
    
# st.markdown('welcome to chai app')
# st.markdown('>blockquote')




#four---------------------------------------------------

# st.title("chai sales dashboard")
# file=st.file_uploader("upload your csv file", type=["csv"])
# if file:
#     df=pd.read_csv(file)
#     st.subheader("data preview")
#     st.dataframe(df)
    
# if file:
#     st.subheader("summary states")
#     st.write(df.describe())

# if file:
#     cities=df["cities"].unique()
#     selected_city=st.selectbox("filter by cities",cities)
#     filtered_data=df[df["city"]==selected_city]
#     st.dataframe(filtered_data)



#five--------------------------------
# import requests
# st.title("live currency converter")
# amount=st.number_input("enter the amout of inr",min_value=1)
# target_currency=st.selectbox("convert to ",["usd","eur","gbp","jpy"])
# if st.button("convert"):
#     url=""
#     response=requests.get()(url)
#     if response.status_code==200:
#         data=response.json( )
#         rate=data["rates"][target_currency]
#         converted=rate*amount
#         st.success(f"{amount} inr={converted:.2f}{target_currency}")
#     else:
#         st.error("failed to fetch")
