import requests
import json



url = "http://47.102.118.1:8089/api/challenge/record/faffa1cf-b298-452b-b469-d48f8ddf57a0"
data = requests.get(url)
result = data.json()
print(result)
