from .api_client import APIClient
from .endpoints import ERCEndpoints

class ERCSDK:
    def __init__(self, base_url, api_key):
        self.client = APIClient(base_url, api_key)
        self.endpoints = ERCEndpoints(self.client)