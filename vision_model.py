import os
import google.generativeai as genai
import PIL

# IMPORTANT : Hide this key before pushing this code to a public repo
# Initialise GOOGLE_API_KEY env variable by using the MakerSuite API key
os.environ['GOOGLE_API_KEY'] = '<your key here>'
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# For text and/or image inputs, create an instance of gemini-pro-vision model
vision_model = genai.GenerativeModel('gemini-pro-vision')

# Pass an image to the vision model and prompt it
image = PIL.Image.open('assets/sample_image.png')
response = vision_model.generate_content(['Explain the picture', image])

# Only show the text response to the prompt
print(response.text)

# View all attributes in the response object
# print(vars(response))