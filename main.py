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
        div [data-testid="stVerticalBlock"] {
            boredr: 5px;
        }
        footer {visibility : hidden;}
        #irregular-verbs-quiz {font-size: calc(1.4rem + .8vw); font-weight: 700;};
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

if 'another_answer' not in st.session_state:
    st.session_state['another_answer'] = None

if 'success' not in st.session_state:
    st.session_state['success'] = None

with st.sidebar:
    st.header(f'Hi There!')
    st.subheader("Download irregular verbs here👇")
    with open("./list-of-irregular-verbs.pdf", "rb") as file:
        btn = st.download_button(
            label="Download PDF📁",
            data=file,
            file_name="Irregular Verbs.pdf",
            mime="image/png"
        )


def streak_count():
    i = 0
    streak = 0
    while True:
        i -= 1
        if st.session_state['data_question'][i] == 1:
            streak += 1
        else:
            break
    return streak


streak = streak_count()
if streak == 5 or streak == 10 or streak == 15 or streak == 20 or streak == 25:
    rain('🔥', 50, 5, 1)

colored_header(
    label="Irregular Verbs Quiz🚀✍👨‍🎓",
    description='',
    color_name="blue-60",
)


container = st.container()
with container:
    col3, col4 = st.columns([5, 2], gap='small')
    with col3:
        st.subheader(st.session_state['question'])

    answer = st.text_input("Answer", max_chars=20,
                           key='ans', placeholder='understood...')
    col1, col2, c, = st.columns([1, 2, 3])
    with col1:
        submit = st.button("📌Submit")
    with col2:
        next_question = st.button("🔎Next question")

    if next_question and st.session_state['submit']:
        st.session_state['success'] = None
        st.session_state['question'], st.session_state['answer'] = get_random_question(
            st.session_state['df'])
        st.session_state['submit'] = False
        st.experimental_rerun()

    if submit and st.session_state['submit'] == False and answer != '':
        st.session_state['submit'] = True
        answers = st.session_state['answer'].split('/')
        for ans in answers:
            if answer.lower() == ans.lower():
                st.session_state['success'] = True
                st.session_state['data_question'].append(1)
                if len(answers) == 2:
                    if answers[1] == ans:
                        st.session_state['another_answer'] = answers[0]
                    else:
                        st.session_state['another_answer'] = answers[1]
                else:
                    st.session_state['another_answer'] = None
                break
        else:
            st.session_state['data_question'].append(0)
            st.session_state['success'] = False

    if st.session_state['success'] == True:
        st.success("That is right!!", icon='✅')
        if st.session_state['another_answer']:
            st.info(
                f"Anthor answer is {st.session_state['another_answer']}", icon='👨‍🎓')
    elif st.session_state['success'] == False:
        answer = st.session_state['answer']
        st.error(
            f"wrong the right answer is {answer}", icon='❌')
    with col4:
        col5, col6 = st.columns(2)
        with col5:
            streak = streak_count()
            string = f"<span style = 'font-size: 1.35rem; font-weight: 600; line-height:2.4;'>🔥 {streak}</span>"
            st.write(string, unsafe_allow_html=True)
        with col6:
            correct_answer = str(st.session_state['data_question'].count(1))
            all_answer = str(len(st.session_state['data_question'])-1)
            string = f"<span style = 'font-size: 1.35rem; font-weight: 600; line-height:2.4;'>{correct_answer} of {all_answer}</span>"
            st.write(string, unsafe_allow_html=True)


show_pages(
    [
        Page("./main.py", "Quiz", "🚀"),
        Page("./pages/about.py", "About", "💻"),
        Page("./pages/contact_me.py", "Contact Me", "📬"),
    ]
)
