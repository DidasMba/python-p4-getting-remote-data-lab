import requests
import pytest
from lib.get_requester import GetRequester

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return response_body.json()  # Corrected line
        except ValueError:
            # Handle the case where the response is not a valid JSON
            print("Error: Unable to parse response as JSON.")
            return None

def test_get_response():
    '''get_response_body function returns response.'''
    requester = GetRequester(URL)
    actual_response = requester.get_response_body().decode('utf-8')  # Decode bytes to string
    assert actual_response == JSON_STRING
