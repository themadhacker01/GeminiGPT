import os
import google.generativeai as genai


# IMPORTANT : Hide this key before pushing this code to a public repo
# Initialise GOOGLE_API_KEY env variable by using the MakerSuite API key
os.environ['GOOGLE_API_KEY'] = '<enter key here>'
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# For text only inputs, create an instance of gemini-pro model
model = genai.GenerativeModel('gemini-pro')

# Prompting the gemini-pro model, an example
response = model.generate_content('List 5 planets each with an interesting fact')

# View all attributes in the response object
# print(vars(response))

# Only show the text response to the prompt
print(response.text)