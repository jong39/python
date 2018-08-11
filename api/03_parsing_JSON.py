import requests
import json

BASE_URL = "https://reqres.in"
param = {'page': 2}
response = requests.get(BASE_URL + "/api/users", params=param)
# print(response)
# print(response.json())
print(json.dumps(response.json(), indent=4))

resp = response.json()
# import ipdb; ipdb.set_trace()
print("Total pages: ", resp["total_pages"])
