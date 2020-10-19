import base64


def match(subPic, pic):
    with open(subPic, "rb") as f:  # 转为二进制格式
        base64_data1 = base64.b64encode(f.read())  # 使用base64进行加密

    with open(pic, "rb") as f:  # 转为二进制格式
        base64_data2 = base64.b64encode(f.read())  # 使用base64进行加密

    if base64_data1 == base64_data2:
        return True
    else:
        return False
