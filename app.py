import streamlit as st
from multiapp import MultiApp
from PIL import Image
from images import * # import your app modules here

st.sidebar.markdown('# **Telecom Bussiness Analysis**')
st.sidebar.markdown("""
Before investing on a business it is a must to have best understanding about the field. This project is all about analyzing TellCo's user and find out whether it is worth buying or selling.
""")

# Add all your application here
select_events=st.selectbox(label='Telecom data analysis', options=['user_overview analysis', 'user_engagement analysis', 'user_experience', 'user_satisfaction'])
submitted=st.button('submit')

if(select_events=='user_overview analysis'):
    st.subheader("top 10 handsets")
    image=Image.open('./images/top 10 handset.png')
    st.image(image, caption='')
    st.subheader("top 3 hand set manufacturer")
    image=Image.open('./images/handset manufacturer.PNG')
    st.image(image, caption='')


if(select_events=='user_engagement analysis'):
    st.subheader("top 3 apps customers engage with.PNG")
    image=Image.open('./images/top 3 apps customers engage with.PNG')
    st.image(image, caption='')

    st.subheader("maximum custermer engagement among 3 clusters")
    image=Image.open('./images/maximum custermer engagement among 3 clusters.PNG')
    st.image(image, caption='')


