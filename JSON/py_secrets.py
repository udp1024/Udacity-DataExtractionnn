# an app template to manage app secrets on the local system keyring
# base assumption: keyring does not have a password set

# Using the system keyring
import keyring

service_id = "my_nyt_app"
username  = 'dustin'
secretpw = 'some-secret-string'
MAGIC_USERNAME_KEY = 'im_the_magic_username_key'

keyring.set_password(service_id, username, secretpw)
keyring.set_password(service_id, MAGIC_USERNAME_KEY, username)

# to retrieve secrets
username = keyring.get_password(service_id, MAGIC_USERNAME_KEY)
password = keyring.get_password(service_id, username)

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
if ("MY_APP_USERNAME" in os.environ):
    # the second parameter, 'localhost', is the default to use if the variable is not retrieved 
    myAppUsername = os.getenv('MY_APP_USERNAME', 'localhost')
    user = os.getenv('MY_APP_DB_USER', 'myapp')
    password = os.getenv('MY_APP_DB_PASSWORD', '')

