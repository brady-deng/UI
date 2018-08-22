from aip import AipSpeech,AipOcr
APP_ID = '11702208'
API_KEY = 'A2PICecu9tMyZcHb773oFqWf'
SECRET_KEY = '1Pld9D8Ubbbvv7Xaxeg65iK91UAZUKwj '
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('2.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """


""" 调用通用文字识别（含生僻字版）, 图片参数为本地图片 """
client.enhancedGeneral(image)

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（含生僻字版）, 图片参数为本地图片 """
print(client.basicGeneral(image, options))

# url = "https//www.x.com/sample.jpg"
#
# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)
