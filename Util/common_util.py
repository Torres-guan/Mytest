# coding: utf-8 
import operator
import json
class commonUtil:
	
	def is_contain(self, str_one, str_two):
		'''
		判断一个字符串是否在另一个字符串中
		str_one:查找的字符串
		str_two：被查找的字符串
		'''
		flag = None
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag


	def is_equal(self, dict_one, dict_two):
		'''
		判断两个字典是否相等
		'''
		if isinstance(dict_one, str):
			dict_one = json.loads(dict_one)
		if isinstance(dict_two, str):
			dict_two = json.loads(dict_two)
		result = operator.eq(dict_one, dict_two)
		return result

if __name__ == '__main__':
	a = {
		"name":"guan",
		"age":"25"
	}
	b = {
		"name":"guan",
		"age":"25"
	}
	com = commonUtil()
	c = com.is_equal(a,b)
	print(c)
