# coding: utf-8 
import requests
import json
from Util.operation_json import OperationJson

class operationHeader(object):
	
	def __init__(self, respons):
		self.respons = json.loads(respons)
	
	def get_respons_url(self):
		#获取登陆返回的token的url
		url = self.respons['data']['url'][0]
		return url
		
	def get_cookie(self):
		#获取cookie的jar文件
		url = self.get_respons_url()+''
		cookie = requests.get(url).cookies
		return cookie

	def write_cookie(self):
		cookie = requests.utils.dict_from_cookiejar(self.get_cookie)
		op_json = OperationJson()
		op_json.write_data(cookie)

if __name__ == '__main__':
	url = 'http://m.imooc.com/passport/user/login'
	data = {
		"uesrname":"41858144@qq.com",
		"password":"12002103gx",
		"verify":"",
		"referer":"https://m.imooc.com"
	}
	res = requests.post(url, data).json()
	print(res)