import streamlit as st
from langchain.llms import OpenAI
import os
from langchain_openai import ChatOpenAI
os.environ["OPENAI_API_KEY"] = "sk-proj-kPX9DYERUZ7tvgm1FykqT3BlbkFJJbniRUV3Km3ionngjTZE"

st.title('🦜🔗 Quickstart App')

openai_api_key = "sk-proj-kPX9DYERUZ7tvgm1FykqT3BlbkFJJbniRUV3Km3ionngjTZE"

def generate_response(input_text):
    llm = ChatOpenAI(model="ft:gpt-3.5-turbo-1106:yethi-consulting-pvt-ltd:1:9nMccwQZ", temperature=1)
    # llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text).content
    st.info(response)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'Do you get time to read ?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)