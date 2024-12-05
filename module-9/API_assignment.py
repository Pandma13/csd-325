# Megan Wheeler
# Assignment 8.2
# 5 December 2024

import requests
import json

# test connection to API
response = requests.get("https://www.dnd5eapi.co/api/")
print(response.status_code)

# print response with no formatting
print(response.json())

# print response with formatting from API tutorial
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())