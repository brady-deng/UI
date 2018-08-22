from aip import AipSpeech
APP_ID = '11388941'
API_KEY = '0ZYGXXiNUMXDalelafeEL0GW'
SECRET_KEY = 'VmTREEGWKm4V0DPAyQLfuEwhwISZoXx6 '
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 识别本地文件
temp1 = client.asr(get_file_content('life.wav'), format='wav', rate=16000,options= {
    'dev_pid': 1737,
})
# temp2 = client.asr(get_file_content('2.amr'), format='amr', rate=8000,options= {
#     'lan': 'en',
# })

print(temp1['result'])
# print(temp2['result'])
#
with open("res.txt",'w') as file:
    file.write(temp1['result'][0])
#     file.write(temp2['result'][0])
