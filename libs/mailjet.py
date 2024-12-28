from mailjet_rest import Client
from dataclasses import dataclass

from core.settings_base import MAILJET

@dataclass
class MailClient:
    api_key = MAILJET["APIKEY_PUBLIC"]
    api_secret = MAILJET["APIKEY_PRIVATE"]
    version="v3.1"
    client = Client(auth=(api_key, api_secret), version=version)

    # send en email via mailjet
    def send_message(self, data):
        return self.client.send.create(data=data)
