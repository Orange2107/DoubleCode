import requests
import json

#start接口：开始获取题目信息

def data(challengeUuid):
    url = 'http://47.102.118.1:8089/api/challenge/start/'+ challengeUuid
    id = 39
    token = "038bcb76-b65c-4641-9c7e-89a3c1b66a41"
    dit = {"teamid": id, "token": token}
    result = requests.post(url=url, json=dit).text
    result1 = json.loads(result)
    return result1

