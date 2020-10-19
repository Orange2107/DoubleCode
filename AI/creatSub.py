import requests
import json

url = 'http://47.102.118.1:8089/api/challenge/create'
id = 39
letter = 'v'
token = "038bcb76-b65c-4641-9c7e-89a3c1b66a41"
dit = {"teamid": id,
       "data": {
           "letter": letter,
           "exclude": 5,
           "challenge": [
               [1, 3, 2],
               [9, 7, 0],
               [8, 6, 4]
           ],
            "step": 4,
           "swap": [1,5],
       },
       "token": token
       }
result = requests.post(url=url, json=dit)
print(result.text)
