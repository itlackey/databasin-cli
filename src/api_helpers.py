import requests
from pprint import pprint


def get_api_data(url):
    api_key = "YOUR_API_KEY"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    pprint(data)