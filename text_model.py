import os
import google.generativeai as genai
import PIL

# IMPORTANT : Hide this key before pushing this code to a public repo
# Initialise GOOGLE_API_KEY env variable by using the MakerSuite API key
os.environ['GOOGLE_API_KEY'] = '<your key here>'
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# For text only inputs, create an instance of gemini-pro model
text_model = genai.GenerativeModel('gemini-pro')

# Prompting the gemini-pro model, an example
response = text_model.generate_content('Tell me about Bangalore as a city?')

# Only show the text response to the prompt
print(response.text)

# View all attributes in the response object
# print(vars(response))