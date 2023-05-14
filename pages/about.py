import streamlit as st
from streamlit_extras.colored_header import colored_header

st.set_page_config('About💻', layout='centered')

with st.sidebar:
    st.header(f'Welcome!')
    st.subheader("Download the irregular verbs Here:")
    st.download_button(
        "Downlod PDF", data='./list-of-irregular-verbs.pdf', file_name='irregular_verbs.pdf')

descp = """Introducing the Irregular Verb Quizzer, a simple and engaging app developed by student Mohamad Bashar and supervised by teacher Alaa Hamdan. This app helps students memorize irregular verbs in a fun and interactive way.
The user-friendly interface caters to learners of all levels, making it easy for everyone to practice and improve their knowledge of irregular verbs."""
colored_header(label="Irregular Verbs Quiz💎👍", description='')
st.write(descp)
