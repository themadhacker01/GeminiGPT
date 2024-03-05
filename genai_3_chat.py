import os
import google.generativeai as genai
import PIL

# IMPORTANT : Hide this key before pushing this code to a public repo
# Initialise GOOGLE_API_KEY env variable by using the MakerSuite API key
os.environ['GOOGLE_API_KEY'] = '<your key here>'
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# For text only inputs, create an instance of gemini-pro model
text_model = genai.GenerativeModel('gemini-pro')

chat = text_model.start_chat(history=[])

# Prompting the gemini-pro model, an example
response = chat.send_message('Is the Karnataka govt becoming anti-migrant')

# Only show the text response to the prompt
print(response.text)

# View all attributes in the response object
# print(vars(response))

# Send another prompt, to test chat history
response = chat.send_message('What is the best place to startup in India - Bangalore or Hyd')
print(response.text)

# Chat stores prompt-response pairs sequentially
print(chat.history)