# Q&A Chatbot
from langchain_openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv # take environment variables from .env
load_dotenv()

# Function to create openai model & get response
# openai_api_key=os.getenv("OPEN_API_KEY"), 
# openai_api_key='sk-proj-jea8EMstMua4C27xavNET3BlbkFJ95IgtpMGIqHYbvnNcgft'
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),
                 model_name='gpt-3.5-turbo-instruct', 
                 temperature=0.5)
    response = llm(question)
    return response

# Initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input=st.text_input("Input: ", key=input)
response = get_openai_response(input)

submit = st.button("Submit")

# if submit button is clicked
if submit:
    st.subheader("The response is")
    st.write(response)
    