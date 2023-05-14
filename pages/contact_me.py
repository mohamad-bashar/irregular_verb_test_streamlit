import streamlit as st
import smtplib as smtp
import ssl
import os
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
from markdownlit import mdlit

st.set_page_config(layout="centered", page_title="Contact Me📬")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            p {font-size: 1.2rem;}
            #contact-me {font-size: calc(1.8rem + .6vw);}
            .viewerBadge_container__1QSob {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

i = False


def send_mail(email, msg):
    user_name = "mohamadbashar07@gmail.com"
    user_pass = os.getenv("PASSWORD")
    receiver = "mohamadbashar07@gmail.com"

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    massage = f"""\
Subject: Email From {email}
From {email}
{msg}"""

    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, user_pass)
        server.sendmail(user_name, receiver, massage)


colored_header(
    label="📬Contact Me",
    description='',
    color_name="orange-70",
)
with st.form(key="email_form"):
    mdlit("Make sure of your [green]email ✔[/green]")
    user_email = st.text_input("Enter your email address *")
    message = st.text_area("Enter your message *")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_mail(user_email, message)
        i = True
        rain(
            emoji="👍",
            font_size=32,
            falling_speed=10,
            animation_length=1,
        )


if i:
    st.success(body="Your message was sent successfully!", icon="✔")
