import streamlit as st
import pandas as pd
import numpy as np
import smtplib

from PIL import Image
import os



# image = Image.open('sunrise.jpg')

# st.image(image, caption='Sunrise by the mountains')
path = [ os.path.join('images',x) for x in os.listdir('images')]
names = [x.split('.')[0]  for x in os.listdir('images')]

path.sort()
names.sort()

images = [ Image.open(x) for x in path]



st.image(images,caption=names,width=200)
with st.sidebar:
    with st.form('Form1'):
        pick_img = st.radio("Which one?", 
                names)
        #st.selectbox('Select flavor', ['Vanilla', 'Chocolate'], key=1)
        text_input = st.text_input(label='Any extra requirements?')
        submit = st.form_submit_button('Submit')
gmail_user =  st.secrets["user"]
gmail_password =  st.secrets["pwd"]

FROM = gmail_user

TO = [gmail_user] 

SUBJECT = "what you should wear"

# do something with what the user selected here
if submit:

    TEXT = str(pick_img)+str(text_input)
    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(FROM, TO, message)
    st.sidebar.success('Sure!(^Д^)')
    server.quit()
