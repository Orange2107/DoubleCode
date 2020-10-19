from PIL import Image
import os

CfileList = []
SfileList = []

def eachFile(filepath, list):
    pathDir =os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        list.append(child)
eachFile(r'.\无框字符', CfileList)
eachFile(r'.\分割字符', SfileList)

for cfn, sfn in zip(CfileList, SfileList):
    filename = cfn
    img = Image.open(filename)
    size = img.size
            # 准备将图片切割成9张小图片
    weight = int(size[0] // 3)
    height = int(size[1] // 3)
    cnt = 0
    for j in range(3):
        for i in range(3):
             cnt+=1
             box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
             region = img.crop(box)
             region.save(sfn+'\\{}.jpg'.format(cnt))

def cutPicture(cFile, sFile):
    filename = cFile
    img = Image.open(filename)
    size = img.size
    # 准备将图片切割成9张小图片
    weight = int(size[0] // 3)
    height = int(size[1] // 3)
    cnt = 0
    for j in range(3):
        for i in range(3):
            cnt += 1
            box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
            region = img.crop(box)
            region.save(sFile + '\\{}.jpg'.format(cnt))
