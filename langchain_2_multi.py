import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

os.environ['GOOGLE_API_KEY'] = '<your key here>'

llm = ChatGoogleGenerativeAI(model = 'gemini-pro-vision')
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
