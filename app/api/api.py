import requests
import json

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(url)

    print(response.text)
