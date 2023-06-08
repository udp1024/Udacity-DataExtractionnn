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

