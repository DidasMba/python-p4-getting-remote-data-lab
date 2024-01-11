import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return response.json()
        except ValueError:
            # Handle the case where the response is not a valid JSON
            print("Error: Unable to parse response as JSON.")
            return None
