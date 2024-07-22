import streamlit as st
from langchain.llms import OpenAI
import os
from langchain_openai import ChatOpenAI
from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-2uGtEjNF6PFHSrT5Yhu8T3BlbkFJHy5kALQ9CmnyOOQpAwCX"
openai_api_key = "sk-proj-2uGtEjNF6PFHSrT5Yhu8T3BlbkFJHy5kALQ9CmnyOOQpAwCX"
st.title('🦜🔗 Replies in Sam Altam Style')# 
client = OpenAI()

def generate_response(input_text):
    llm = ChatOpenAI(model="ft:gpt-3.5-turbo-1106:yethi-consulting-pvt-ltd:1:9nMccwQZ", temperature=0.5,openai_api_key=openai_api_key)
    # llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text).content
    st.info(response)

def return_sam_style(input_text):
    completion = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-1106:yethi-consulting-pvt-ltd:1:9nMccwQZ",
      messages=[
        {"role": "system", "content": "Imagine you are Sam Altman. Respond to the following query in a conversational manner, ensuring the answer is comprehensive and engaging, suitable for a general audience. Make sure to address the specific topic given in the query and provide clear, insightful answers."},
        {"role": "user", "content":input_text}
      ]
    )
    return st.info(completion.choices[0].message.content)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'where do you think AI will be in 5 years ?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        return_sam_style(text)
        # generate_response(text)