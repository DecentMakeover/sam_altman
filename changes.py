import streamlit as st
from langchain.llms import OpenAI
import os
from langchain_openai import ChatOpenAI
from openai import OpenAI
import os
import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate

st.title('🦜🔗 Replies in Sam Altam Style')# 
client = OpenAI()
embeddings = OpenAIEmbeddings()
text_splitter = SemanticChunker(embeddings)
splits = text_splitter.create_documents([file_content])
# vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
vectorstore = Chroma(persist_directory="./chroma_db",embedding=OpenAIEmbeddings())
# vectorstore = Chroma.from_documents(persist_directory = './' ,documents=splits, embedding=OpenAIEmbeddings())





# template = """Imagine you are Sam Altman. Respond to the following query in a conversational manner, 
# ensuring the answer is comprehensive and engaging, suitable for a general audience.
# Make sure to address the specific topic given in the query and provide clear, 
# insightful answers. Use the context below if needed to answer the question ,
# if the context is not useful you can choose to ignore the context

# {context}

# Question: {question}

# Helpful Answer:"""
# custom_rag_prompt = PromptTemplate.from_template(template)

# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

# def return_output(vectorstore,llm , input_text):
#     retriever = vectorstore.as_retriever()
#     prompt = hub.pull("rlm/rag-prompt")
#     rag_chain = (
#         {"context": retriever | format_docs, "question": RunnablePassthrough()}
#         | custom_rag_prompt
#         | llm
#         | StrOutputParser()
#     )
#     output = rag_chain.invoke(input_text)
#     return output

# def generate_response(input_text):
#     llm = ChatOpenAI(model="ft:gpt-3.5-turbo-1106:yethi-consulting-pvt-ltd:1:9nMccwQZ", temperature=0.5,openai_api_key=openai_api_key)
#     # llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#     response = llm(input_text).content
#     st.info(response)

# def return_sam_style(input_text):
#     completion = client.chat.completions.create(
#       model="ft:gpt-3.5-turbo-1106:yethi-consulting-pvt-ltd:1:9nMccwQZ",
#       messages=[
#         {"role": "system", "content": "Imagine you are Sam Altman. Respond to the following query in a conversational manner, ensuring the answer is comprehensive and engaging, suitable for a general audience. Make sure to address the specific topic given in the query and provide clear, insightful answers."},
#         {"role": "user", "content":input_text}
#       ]
#     )
#     return st.info(completion.choices[0].message.content)

# with st.form('my_form'):
#     text = st.text_area('Enter text:', 'where do you think AI will be in 5 years ?')
#     submitted = st.form_submit_button('Submit')
#     if not openai_api_key.startswith('sk-'):
#         st.warning('Please enter your OpenAI API key!', icon='⚠')
#     if submitted and openai_api_key.startswith('sk-'):
#         return_sam_style(text)
#         # generate_response(text)















