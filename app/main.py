import urllib3

from conjur_client import ConjurClient

urllib3.disable_warnings()

client = ConjurClient()

client.authenticate()

username = client.get_secret("aws/database/username")
password = client.get_secret("aws/database/password")

print()
print("Database Username :", username)
print("Database Password :", password)