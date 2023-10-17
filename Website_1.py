#!/usr/bin/env python
# coding: utf-8

import sys  # Add this line to import the 'sys' module
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/f77e68a2-c9d7-4645-bb09-454921abdc29/haQmAzZdf4.json")

# GitHub image URLs
img_contact_form_url = 'https://raw.githubusercontent.com/SonOfGod04/website/main/Screenshot%20(120).png'
img_model = 'https://raw.githubusercontent.com/SonOfGod04/website/main/Screenshot%20(127).png'
img_Analysis = 'https://raw.githubusercontent.com/SonOfGod04/website/main/Screenshot%20(129).png'

# Header section
st.subheader("Hi, I am Miracle Saliu :wave:")
st.title("A Data Scientist From Nigeria")
st.write("I am passionate about finding ways to use Python, R, and SQL to be more efficient and effective in business settings")
st.write("[Learn More >](https://github.com/SonOfGod04)")

# What I Do
st.write("-----")
left_column, right_column = st.columns(2)
with left_column:
    st.header("What I Do")
    st.write("##")
    st.write(
        """
        - I specialize in empowering aspiring data scientists by providing comprehensive guidance, particularly in areas where they may face challenges. I believe in walking hand-in-hand with them on their journey to a deeper understanding of data science.
        - For students seeking to excel in their projects, I offer not only meticulous analysis but also expert guidance in selecting the most suitable algorithms. My aim is to help students achieve top grades in their projects, opening up a world of opportunities.
        - My proficiency in data science and data analysis extends to driving strategic decision-making and enhancing business performance. I transform data into actionable insights that steer organizations toward success.
        - Furthermore, I harness my skills to tackle network intrusion issues, offering effective solutions to fortify defenses against data breaches. I'm committed to contributing to the ongoing battle against data intrusions.
        - With a background in the medical field, I also utilize my expertise to provide solutions. For instance, I assist users of menstrual apps in making informed choices and address various medical-related challenges.
        
        If any of these areas align with your organization's needs, I am eager to join your team. I am dedicated to both enhancing my skills and contributing to the growth of your company, ultimately benefiting humanity as a whole.
        """
    )
    st.write("[Github Account >](https://github.com/SonOfGod04)")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

st.write("---")

# My Projects
st.header("My Projects")
st.write("##")
image_column, text_column = st.columns((1, 2))

with image_column:
    st.image(img_contact_form_url)  # Fixed variable name
with text_column:
    st.subheader("Easily Deploy Your Expertly Built Models")
    st.write(
        """
        Deploying your model is a pivotal step that not only evaluates its performance in a production environment but also enables effective communication of your ideas with your intended audience.

        By deploying your model, you gain the ability to access and enhance it whenever necessary, ensuring that it remains a dynamic and valuable asset to your projects and goals.
        """
    )
    st.markdown("[See Samples...](https://student-performance-01.streamlit.app)")

st.write("---")

image_column, text_column = st.columns((1, 2))

with image_column:
    st.image(img_model)
with text_column:
    st.subheader("Craft a Data Science Project that Speaks for Itself")
    st.write(
        """
        Creating a detailed data science project is crucial for better understanding. It also allows you to use machine learning to provide real solutions.
        """
    )
    st.markdown("[See Samples...](https://github.com/SonOfGod04/Network-Intrusion-KDDP-dataset/blob/main/KDDCUP99N.ipynb)")

st.write("---")

image_column, text_column = st.columns((1, 2))

with image_column:
    st.image(img_Analysis)
with text_column:
    st.subheader("Detailed Data Analysis Project")
    st.write(
        """
        A thorough and comprehensive data analysis is essential for gaining a better understanding of your business. It helps you dive deep into the reasons behind your business's current state and provides insights on how to enhance and optimize it for improvement.
        """
    )
    st.markdown("[See Samples...](https://github.com/SonOfGod04/Student-Performance/blob/main/Student_Prediction12.ipynb)")

# Contact
st.write("----")
st.header("Get In Touch With Me!")
st.write("##")

# Add the contact form
contact_form = """
<style>
    .contact-form {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f0f0f0;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }
    
    .contact-form input[type="text"],
    .contact-form input[type="email"],
    .contact-form textarea {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    
    .contact-form button {
        background-color: #007BFF;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
</style>

<div class="contact-form">
    <form action="https://formsubmit.co/saliumiracleg@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
</div>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
