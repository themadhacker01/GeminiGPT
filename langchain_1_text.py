import os

# Langchain has integrated the gemini model into its system using the ChatGoogleGenerativeAI class
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialise the environment variable with the API key
os.environ['GOOGLE_API_KEY'] = '<your key here>'

# To use a text only model, create an instance of gemini-pro
llm = ChatGoogleGenerativeAI(model = 'gemini-pro')
response = llm.invoke('Explain quantum computing in 50 words')

# print(response.content)

# Ask multiple prompts sequentially, and receive seperate responses
batch_responses = llm.batch([
    'Name the top 5 engg colleges in India',
    'Of these, which college is the best for CS?'
])

for res in batch_responses:
    print(res.content)