import requests
import json

import requests
import json

def mistral_endpoint(query):
    url = f'http://127.0.0.1:8000/mistral?query={query}'

    response = requests.get(url,stream=True)

    if response.status_code == 200:
        asstext = ""
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                asstext += chunk.decode('utf-8')
        return asstext
    else:
        print(f'Request failed with status code {response.status_code}')
        return None


if __name__ == '__main__':
    query = input('Enter your query: ')
    mistral_endpoint(query)