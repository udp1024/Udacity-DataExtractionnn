# using a .env file
# pip install python-dotenv
# touch nytime.env
# add following lines of text to it
#   API_KEY=test-key
#   API_SECRET=test-secret
# 
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

print("API_KEY: ", api_key)
print("API_SECRET: ", api_secret)
