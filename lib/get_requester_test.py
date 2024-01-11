# Import necessary modules and the class you want to test
import pytest
from lib.get_requester import GetRequester

# Define test data or constants
URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = '[{"name":"Daniel","occupation":"LG Fridge Salesman"},{"name":"Joe","occupation":"WiFi Fixer"},{"name":"Avi","occupation":"DJ"},{"name":"Howard","occupation":"Mountain Legend"}]'

# Write your test functions
def test_get_response():
    '''get_response_body function returns response.'''
    requester = GetRequester(URL)
    actual_response = requester.get_response_body().decode('utf-8')  # Decode bytes to string
    assert actual_response == JSON_STRING
