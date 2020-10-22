import requests
import json

response = requests.get("https://api.ipify.org?format=json")
print(dir(response))
ip = response.json()
print(type(ip))