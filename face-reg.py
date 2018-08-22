from aip import AipSpeech,AipOcr,AipFace
import base64
# -*- coding: utf-8 -*-



APP_ID = '11702269'
API_KEY = 'waphyikGVmZ5sWeyozGbKGUY'
SECRET_KEY = 'QGQB09ic3aMofghWVjFHnMEC1cGtkGkr '
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

##########################################
#人脸检测：检测图片中的人脸并标记出位置信息
##########################################
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


##########################################
#将图片数据编码城base64格式
##########################################
image = get_file_content('2.jpg')
base64_data = base64.b64encode(image)
data1 = base64_data.decode('utf-8')
image = get_file_content('222.jpg')
base64_data = base64.b64encode(image)
data2 = base64_data.decode('utf-8')
# imageType = "BASE64"
#
# """ 调用人脸检测 """
# print(client.detect(data, imageType))
#
# """ 如果有可选参数 """
# options = {}
# options["face_field"] = "age,beauty,faceshape,gender,glasses,race,expression"
# options["max_face_num"] = 3
# options["face_type"] = "LIVE"
#
# """ 带参数调用人脸检测 """
# print(client.detect(data, imageType, options))

##########################################
#人脸注册
##########################################
# image = data
#
# imageType = "BASE64"
#
# groupId = "group1"
#
# userId = "user1"
#
# """ 调用人脸注册 """
# client.addUser(image, imageType, groupId, userId);
#
# """ 如果有可选参数 """
# options = {}
# options["user_info"] = "user's info"
# options["quality_control"] = "NORMAL"
# options["liveness_control"] = "LOW"
#
# """ 带参数调用人脸注册 """
# print(client.addUser(image, imageType, groupId, userId, options))
##########################################
#人脸更新
##########################################
# image = data
#
# imageType = "BASE64"
#
# groupId = "group1"
#
# userId = "user1"
#
# """ 调用人脸更新 """
# client.updateUser(image, imageType, groupId, userId);
#
# """ 如果有可选参数 """
# options = {}
# options["user_info"] = "user's info"
# options["quality_control"] = "NORMAL"
# options["liveness_control"] = "LOW"
#
# """ 带参数调用人脸更新 """
# client.updateUser(image, imageType, groupId, userId, options)
##########################################
#人脸搜索
##########################################
# image = data
#
# imageType = "BASE64"
#
# groupIdList = "group1"
#
# """ 调用人脸搜索 """
# print(client.search(image, imageType, groupIdList))
#
# """ 如果有可选参数 """
# options = {}
# options["quality_control"] = "NORMAL"
# options["liveness_control"] = "LOW"
# options["user_id"] = "user1"
# options["max_user_num"] = 3
#
# """ 带参数调用人脸搜索 """
# print(client.search(image, imageType, groupIdList, options))
##########################################
#获得人脸列表
##########################################
# userId = "user1"
#
# groupId = "group1"
#
# """ 调用获取用户人脸列表 """
# print(client.faceGetlist(userId, groupId))
# groupId = "group1"
#
# """ 调用获取用户列表 """
# client.getGroupUsers(groupId);
#
# """ 如果有可选参数 """
# options = {}
# options["start"] = 0
# options["length"] = 50
#
# """ 带参数调用获取用户列表 """
# print(client.getGroupUsers(groupId, options))
##########################################
#身份验证
##########################################
# image = data
#
# imageType = "BASE64"
#
# idCardNumber = "130984199505010033"
#
# name = "brady"
# """ 调用身份验证 """
# print(client.personVerify(data, imageType, idCardNumber, name))
#
# """ 如果有可选参数 """
# options = {}
# options["quality_control"] = "NORMAL"
# options["liveness_control"] = "LOW"
#
# """ 带参数调用身份验证 """
# print(client.personVerify(image, imageType, idCardNumber, name, options))
##########################################
#人脸对比
##########################################
result = client.match([
    {
        'image': data1,
        'image_type': 'BASE64',
    },
    {
        'image': data2,
        'image_type': 'BASE64',
    }
])
print(result)