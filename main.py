from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.environ['OPENAI_API_KEY']

llm = OpenAI(temperature=0.6)

st.title('Ask me anything!')

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

prompt = st.text_input("Enter your text here and hit Enter:")

if prompt:
    with st.spinner('Generating response...'):
        response = llm(prompt)
        # Add the user's question and the bot's response to the chat history
        st.session_state['chat_history'].append({'user': prompt, 'bot': response})
    st.write(response)

# Display chat history in the sidebar
st.sidebar.title("Chat History")
for chat in st.session_state['chat_history']:
    st.sidebar.markdown(f"**You:** {chat['user']}")
    st.sidebar.markdown(f"**Bot:** {chat['bot']}")