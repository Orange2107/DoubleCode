import transform
import getData
import imgCut
import os
import pictureCompare
import solves
import string
import requests
import json
import getUuidList

if __name__ == "__main__":

    url = "http://47.102.118.1:8089/api/challenge/submit"
    #循环开始测试，知道题目全部解完
    for x in range(len(getUuidList.getUuid())):
        x = 0
        chUuid = getUuidList.getUuid()[0]["uuid"]               #获得题目的uuid
        data1 = getData.data(chUuid)
        swap = data1["data"]["swap"]
        str1 = data1["data"]["img"]
        step = data1["data"]["step"]
        uuid = data1["uuid"]
        id = 39
        token = "038bcb76-b65c-4641-9c7e-89a3c1b66a41"
        initList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        destLayout = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pathList = []
        sPathList = []
        mySwap = [0, 0]
        mySwap[0] = swap[0]
        mySwap[1] = swap[1]
        cSubjectFile = r'.\题目图片\image.jpg'  # 存放转义后的题目图片
        sSubjectFile = r'.\题目切分图片'  # 存放切分为9份的图片
        cutFile = r'.\分割字符'  # 已切分好的无框字符
        BchangeStr = ''
        mark = 0

        transform.trf(str1, cSubjectFile)
        imgCut.cutPicture(cSubjectFile, sSubjectFile)
        pathDir = os.listdir(cutFile)  # 字符名称
        subPathDir = os.listdir(sSubjectFile)  # 题目图片名称

        for dir in pathDir:  # pathList是已经分割好的全部无框字符文件夹路径
            child = os.path.join(cutFile, dir)
            pathList.append(child)

        for dir in subPathDir:  # sPathList是已经分割好的题目字符图片路径
            child = os.path.join(sSubjectFile, dir)
            sPathList.append(child)

        flag1 = -1
        flag2 = -1
        cnt = -1
        for path in pathList:  # 循环查找匹配图片
            cnt += 1
            pathDir1 = os.listdir(path)  # 存放其中一个分割字符的九张图片名称
            pathList1 = []  # 存放字符九张图片的路径
            for dir in pathDir1:
                child = os.path.join(path, dir)
                pathList1.append(child)
            for i in range(9):
                for j in range(9):
                    if pictureCompare.match(pathList1[i], sPathList[j]):
                        flag1 = cnt
                        sP = j
                        break
                else:
                    continue
                break
            if flag1 != -1:
                for i in range(9):
                    if i == sP:
                        continue
                    for j in range(9):
                        if pictureCompare.match(sPathList[i], pathList1[j]):
                            flag2 = 1

            if flag1 != -1 and flag2 == 1:
                break

        ans_char = pathDir[flag1][0]  # ans_char 得到答案
        pathDir1 = os.listdir(pathList[flag1])  # pathDir1是答案字符目录图片名称
        pathList2 = []
        for dir in pathDir1:  # pathList2是已经分割好答案字符图片路径
            child = os.path.join(pathList[flag1], dir)
            pathList2.append(child)
        #获得初始状态序列和目标状态序列：
        for i in range(9):
            for j in range(9):
                if pictureCompare.match(sPathList[i], pathList2[j]):
                    initList[i] = j + 1
        str1 = ''
        for i in range(9):
            str1 = str1 + '%d' % initList[i]
        str2 = ''
        for i in range(9):
            if initList[i] == 0:
                continue
            else:
                destLayout[initList[i] - 1] = initList[i]
        for i in range(9):
            str2 = str2 + '%d' % destLayout[i]

        ans_str = ''  # 操作序列
        #获得操作序列，我的交换，每一步状态
        ans_str, mySwap, lst_steps = solves.getAnswer(str1, str2, step, swap)

        #submit接口：提交答案
        msg = {"uuid": uuid, "teamid": id, "token": token, "answer": {"operations": ans_str, "swap": mySwap}}
        result = requests.post(url=url, json=msg)
        result1 = json.loads(result.text)
        print(result.text)

