import requests

url = "https://employability-portal.gupy.io/api/v1/jobs?"

params = {"jobName": "dados"}
response = requests.get(url, params = params)

# data = response.json()

# print(data.get("pagination"))

data = response.json()
pagination = data.get("pagination", {})

total = pagination.get("total", 0)
limit = pagination.get("limit", 0)
offset = pagination.get("offset", 0)


total_posicoes = total / limit
if total_posicoes % 1 != 0:
    total_posicoes = int(total_posicoes) + 1

total_offset = total_posicoes - 1

print("total:", total)
print("limit:", limit)
print("offset:", offset)
print("total_posicoes:", total_posicoes)
print("total_offset:", total_offset)