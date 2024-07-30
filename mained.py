__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_community.vectorstores.chroma import Chroma
import streamlit as st




st.title('🦜🔗 Replies in Sam Altam Style')# 
llm = ChatOpenAI(model="ft:gpt-3.5-turbo-1106:yethi-consulting-pvt-ltd:1:9nMccwQZ")

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"The file at {file_path} was not found."
    except Exception as e:
        return str(e)

# Example usage
file_path = 'wikipedia-sam.txt'  # Replace with the path to your text file
embeddings = OpenAIEmbeddings()
text_splitter = SemanticChunker(embeddings)

template = """Imagine you are Sam Altman. Respond to the following query in a conversational manner, 
ensuring the answer is comprehensive and engaging, suitable for a general audience.
Make sure to address the specific topic given in the query and provide clear, 
insightful answers. Use the context below if needed to answer the question ,
if the context is not useful you can choose to ignore the context

{context}

Question: {question}

Helpful Answer:"""
custom_rag_prompt = PromptTemplate.from_template(template)
file_content = read_text_file(file_path)
sam_splits = text_splitter.create_documents([file_content])
vectorstore = Chroma.from_documents(persist_directory = './' ,documents=sam_splits, embedding=OpenAIEmbeddings())
vectorstore.persist()
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def return_output(vectorstore,llm , input_text):
    retriever = vectorstore.as_retriever()
    prompt = hub.pull("rlm/rag-prompt")
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | custom_rag_prompt
        | llm
        | StrOutputParser()
    )
    output = rag_chain.invoke(input_text)
    return st.info(output)


with st.form('my_form'):
    text = st.text_area('Enter text:', 'where do you think AI will be in 5 years ?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        return_output(vectorstore , llm , text)
