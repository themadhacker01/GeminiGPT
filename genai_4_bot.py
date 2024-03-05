import os
import streamlit as st
import google.generativeai as genai

st.title('Gemini Bot')

# Initialise the env with the API key and setup the GenAI instance
os.environ['GOOGLE_API_KEY'] = '<your key here>'
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# Selecting gemini-pro for text only interaction
model = genai.GenerativeModel('gemini-pro')

# Initialise chat history for the bot
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            'role': 'Assistant',
            'content': 'Ask me anything'
        }
    ]

# Display chat messages from history on app re-launch
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# Process and store query and response
def llm_function(query):
    response = model.generate_content(query)

    # Displaying the assistant message
    with st.chat_message('assistant'):
        st.markdown(response.text)
    
    # Storing the user message
    st.session_state.messages.append(
        {
            'role': 'user',
            'content': query
        }
    )

    # Storing the assistant message
    st.session_state.messages.append(
        {
            'role': 'assistant',
            'content': response.text
        }
    )

# Accept user input from the UI
query = st.chat_input('What\'s up')

# Calling the function when input is provided
if query:
    with st.chat_message('user'):
        st.markdown(query)
    
    llm_function(query)
