# Using the Env Variables
# os.environ behaves like a python dictionary, so all the common dictionary operations can be performed. 
# In addition to the get and set operations mentioned in the other answers, we can also simply check if a key exists. 
# The keys and values should be stored as strings.

import os

# set environment variable
os.environ["MY_APP_USERNAME"] = username
os.environ["MY_API_TOKEN"] = "my token"
os.environ["MY_PUB_KEY"] = "my public key"
os.environ["MY_PV_KEY"] = "my private key"

#check if a variable exists in the environ
if ("api_key_nyt" in os.environ):
    # the second parameter, 'localhost', is the default to use if the variable is not retrieved 
    myAppUsername = os.getenv('MY_APP_USERNAME', 'localhost')
    user = os.getenv('MY_APP_DB_USER', 'myapp')
    password = os.getenv('MY_APP_DB_PASSWORD', '')

