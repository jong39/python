import requests
import json

BASE_URL = "https://reqres.in"

# response = requests.get(BASE_URL + "/api/users?page=2")

param = {'page' : 2}

response = requests.get(BASE_URL + "/api/users", params=param)

# print(response)
# print(response.json())
print(json.dumps(response.json(), indent=4))