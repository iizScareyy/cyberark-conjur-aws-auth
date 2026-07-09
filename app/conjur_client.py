from urllib.parse import quote

import base64
import requests

from config import (
    CONJUR_URL,
    CONJUR_ACCOUNT,
    CONJUR_LOGIN,
    CONJUR_API_KEY,
)


class ConjurClient:
    def __init__(self):
        self.token = None

    def authenticate(self):
        """
        Authenticate to Conjur using login + API key
        and obtain a short-lived access token.
        """
        login = quote(CONJUR_LOGIN, safe="")
        
        url = (
            f"{CONJUR_URL}/authn/"
            f"{CONJUR_ACCOUNT}/"
            f"{CONJUR_LOGIN}/authenticate"
        )

        response = requests.post(
            url,
            data=CONJUR_API_KEY,
            verify=False
        )

        response.raise_for_status()

        self.token = base64.b64encode(response.content).decode()

        print("✅ Authentication successful")

    def get_secret(self, variable_id):

        url = (
            f"{CONJUR_URL}/secrets/"
            f"{CONJUR_ACCOUNT}/variable/"
            f"{variable_id}"
        )

        headers = {
            "Authorization": f'Token token="{self.token}"'
        }

        response = requests.get(
            url,
            headers=headers,
            verify=False
        )

        response.raise_for_status()

        return response.text