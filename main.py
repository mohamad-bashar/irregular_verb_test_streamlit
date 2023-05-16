import streamlit as st
import pandas as pd
import random
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
from st_pages import Page, show_pages


# Load the CSV file


def load_data():
    df = pd.read_csv("iregular_verbs.csv")
    return df


def get_random_question(df):
    random_index = random.randint(0, len(df) - 1)
    question = df.iloc[random_index]["question"]
    answer = df.iloc[random_index]["answer"]
    return question, answer


st.set_page_config('Quiz🚀', layout='centered')

hide_streamlit_style = """
        <style>
        footer {visibility : hidden;}
        #irregular-verbs-quiz {font-size: calc(1.6rem + .6vw); font-weight: 700;};
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if 'submit' not in st.session_state:
    st.session_state['submit'] = False

if 'df' not in st.session_state:
    st.session_state['df'] = load_data()

if 'data_question' not in st.session_state:
    st.session_state["data_question"] = [0]

if 'question' not in st.session_state:
    st.session_state['question'], st.session_state['answer'] = get_random_question(
        st.session_state['df'])

if 'success' not in st.session_state:
    st.session_state['success'] = None

with st.sidebar:
    st.header(f'Welcome!')

colored_header(
    label="Irregular Verbs Quiz🚀✍👨‍🎓",
    description='',
    color_name="blue-50",
)
i = 0
streak = 0
while True:
    i -= 1
    if st.session_state['data_question'][i] == 1:
        streak += 1
    else:
        break
if streak == 5 or streak == 10 or streak == 15 or streak == 20 or streak == 25:
    rain('🔥', '50', 2, 1)

container = st.container()
with container:
    col3, col4 = st.columns([5, 2], gap='small')
    with col3:
        st.subheader(st.session_state['question'])

    with col4:
        col5, col6 = st.columns(2)
        with col5:
            string = f"<span style = 'font-size: 1.35rem; font-weight: 600; line-height:2.6;'>🔥 {streak}</span>"
            st.write(string, unsafe_allow_html=True)
        with col6:
            correct_answer = str(st.session_state['data_question'].count(1))
            all_answer = str(len(st.session_state['data_question'])-1)
            string = f"<span style = 'font-size: 1.35rem; font-weight: 600; line-height:2.6;'>{correct_answer} of {all_answer}</span>"
            st.write(string, unsafe_allow_html=True)

    answer = st.text_input("Answer", max_chars=20,
                           key='ans', placeholder='understood...')
    col1, col2, c, = st.columns([1, 2, 3])
    with col1:
        submit = st.button("Submit")
    with col2:
        next_question = st.button("Next question")

    if next_question and st.session_state['submit']:
        st.session_state['success'] = None
        st.session_state['question'], st.session_state['answer'] = get_random_question(
            st.session_state['df'])
        st.session_state['submit'] = False
        st.experimental_rerun()

    if submit and st.session_state['submit'] == False and answer != '':
        st.session_state['submit'] = True
        for ans in st.session_state['answer'].split('/'):
            if answer.lower() == ans.lower():
                st.session_state['success'] = True
                st.session_state['data_question'].append(1)
                break
        else:
            st.session_state['data_question'].append(0)
            st.session_state['success'] = False

    if st.session_state['success'] == True:
        st.success("That is right!!", icon='💯')

    elif st.session_state['success'] == False:
        answer = st.session_state['answer']
        st.error(
            f"wrong the right answer is {answer}", icon='❌')


show_pages(
    [
        Page("./main.py", "Quiz", "🚀"),
        Page("./pages/about.py", "About", "💻"),
        Page("./pages/contact_me.py", "Contact Me", "📬"),
    ]
)
