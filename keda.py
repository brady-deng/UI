#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse
import time
import urllib
import json
import hashlib
import base64


def main():
    f = open("2.amr", 'rb')
    file_content = f.read()
    base64_audio = base64.b64encode(file_content)
    body = urllib.parse.urlencode({'audio': base64_audio}).encode(encoding="UTF8")

    url = 'http://api.xfyun.cn/v1/service/v1/iat'
    api_key = 'd138b2fd93d4aa38e7dbe50aea65eaf7'
    param = {"engine_type": "sms8k", "aue": "raw"}

    x_appid = '5b76d562'
    temp = json.dumps(param).replace(' ', '')
    temp = bytes(temp,encoding= "utf-8")
    x_param = base64.b64encode(temp)
    x_time = int(int(round(time.time() * 1000)) / 1000)
    temp = api_key + str(x_time) + bytes.decode(x_param)
    m = hashlib.md5()
    m.update(temp.encode("utf-8"))
    x_checksum = m.hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)

    result = urllib.request.urlopen(req)
    result = result.read()
    print(result)
    return

if __name__ == '__main__':
    main()