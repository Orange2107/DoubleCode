import requests
import json
import  startChallenge
import main

def sub(ans_str):
    url = "http://47.102.118.1:8089/api/challenge/submit"
    uuid = startChallenge.getUuid()
    id = 39
    token = "038bcb76-b65c-4641-9c7e-89a3c1b66a41"
    operations = ans_str
    swap = startChallenge.getSwap()
    dit = {"uuid": uuid,"teamid": id,"token": token,"answer": {"operations": operations, "swap": swap}}
    result = requests.post(url=url, json=dit)
    print(result.text)