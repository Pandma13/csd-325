# Megan Wheeler
# Assignment 8.2
# 5 December 2024

import requests
import json

response = requests.get("http://api.open-notify.org/astros")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())