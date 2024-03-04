import os
import google.generativeai as genai
import PIL

# IMPORTANT : Hide this key before pushing this code to a public repo
# Initialise GOOGLE_API_KEY env variable by using the MakerSuite API key
os.environ['GOOGLE_API_KEY'] = '<your key here>'
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# For text only inputs, create an instance of gemini-pro model
text_model = genai.GenerativeModel('gemini-pro')
vision_model = genai.GenerativeModel('gemini-pro-vision')

# Prompting the gemini-pro model, an example
response = text_model.generate_content('Is the Karnataka govt becoming anti-migrant')

# View all attributes in the response object
# print(vars(response))

# Only show the text response to the prompt
print(response.text)

# Pass an image to the vision model and prompt it
# image = PIL.Image.open('assets/sample_image.png')
# response = vision_model.generate_content(['Explain the picture', image])
# print(response.text)

chat = text_model.start_chat(history=[])
response = chat.send_message('What is the best place to startup in India - Bangalore or Hyd')
print(response.text)

# Chat stores prompt-response pairs sequentially
print(chat.history)