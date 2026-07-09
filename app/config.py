import os
from dotenv import load_dotenv

load_dotenv()

CONJUR_URL = os.getenv("CONJUR_URL")
CONJUR_ACCOUNT = os.getenv("CONJUR_ACCOUNT")
CONJUR_LOGIN = os.getenv("CONJUR_LOGIN")
CONJUR_API_KEY = os.getenv("CONJUR_API_KEY")