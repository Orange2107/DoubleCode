import requests
import json

#rank接口：获取排行

def getRank():
    url = "http://47.102.118.1:8089/api/rank"
    data = requests.get(url)
    result = data.json()
    print(result)

if __name__ == "__main__":
    getRank()