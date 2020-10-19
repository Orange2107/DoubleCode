import requests
import json

#problem接口：获取还未通过的题目

def getUuid():
    url = "http://47.102.118.1:8089/api/team/problem/39"
    result = requests.get(url)
    data = result.json()
    return data


if __name__ == "__main__":
    print((getUuid()))