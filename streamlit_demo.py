from langchain_openai import ChatOpenAI
import streamlit as st

st.title("Ask anything")

with st.sidebar:
    st.title("Provide your OpenAI api key")
    OPEN_API_KEY = st.text_input("OpenAI API key", type="password")

if not OPEN_API_KEY:
    st.info("Enter your OpenAI API key to continue")
    st.stop()

llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

question = st.text_input("Enter the question")

if question:
    response = llm.invoke(question)
    st.write(response)