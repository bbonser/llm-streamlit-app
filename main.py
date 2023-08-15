from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.environ['OPENAI_API_KEY']

st.title('Let me answer anything for you!')
prompt = st.text_input("Enter your text here and hit Enter:")

llm = OpenAI(temperature=0.6)

if prompt:
    response = llm(prompt)
    st.write(response)
