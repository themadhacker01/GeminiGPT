import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Initialising the environment variables
os.environ['GOOGLE_API_KEY'] = '<your key here>'

# Use the gemini-pro-vision model for chat-like interactions
llm = ChatGoogleGenerativeAI(model = 'gemini-pro-vision')

# Create messages in a langchain format
msg = HumanMessage(
    content = [
        {
            'type': 'text',
            'text': 'Find the differences between the 2 pictures'
        },
        {
            'type': 'image_url',
            'image_url': 'https://picsum.photos/id/237/200/300'
        },
        {
            'type': 'image_url',
            'image_url': 'https://picsum.photos/id/219/5000/3333'
        }
    ]
)

response = llm.invoke([msg])
print(response.content)
