import requests

url = "https://employability-portal.gupy.io/api/v1/jobs?"

# headers = {
#     "Authorization": "Bearer YOUR_API_TOKEN"
# }
params = {
    "jobName": "dados",
    # "limit": 12,
    # "offset": 0
}

response = requests.get(url
                        , params=params
                        )

print(response.json())
# "SELECT * FROM jobs WHERE name like '%dados%' LIMIT 400 OFFSET 0"