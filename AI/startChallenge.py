import requests
import json
import getUuidList

url = "http://47.102.118.1:8089/api/challenge/start/" + getUuidList.getUuid()[0]["uuid"]
id = 39
token = "038bcb76-b65c-4641-9c7e-89a3c1b66a41"
dit = {"teamid": id, "token": token}
result = requests.post(url=url, json=dit)
result1 = json.loads(result.text)
chanceleft = result1["chanceleft"]
print(chanceleft)

def getImg():
    return result1["data"]["img"]
def getStep():
    return result1["data"]["step"]
def getSwap():
    return result1["data"]["swap"]
def getUuid():
    return result1["uuid"]
