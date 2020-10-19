import os, base64

def trf(strBase64, sFileName):
        imgdata = base64.b64decode(strBase64)
        file = open(sFileName, 'wb')
        file.write(imgdata)
        file.close()