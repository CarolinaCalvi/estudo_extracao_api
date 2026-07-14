import requests

url = "https://employability-portal.gupy.io/api/v1/jobs?"

params = {"jobName": "dados"}
response = requests.get(url, params = params)

# print(response.json())

data = response.json()

print(data.get("pagination"))