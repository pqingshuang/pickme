import streamlit as st
import pandas as pd
import numpy as np
import smtplib

from PIL import Image
import os



# image = Image.open('sunrise.jpg')

# st.image(image, caption='Sunrise by the mountains')

images = [ Image.open(os.path.join('images',x)) for x in os.listdir('images')]
names = [x.split('.')[0]  for x in os.listdir('images')]
pick_img = st.sidebar.radio("Which one?", 
           names)

st.image(images,caption=names)


FROM = 'monty@python.com'

TO = ["jon@mycompany.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)


    # do something with what the user selected here
if pick_img:
    server = smtplib.SMTP('localhost')
    server.starttls()
    server.sendmail(FROM, TO, message)
    server.quit()