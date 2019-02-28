# -*- coding: utf-8 -*-
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\interfaceTest")
from Base.method import runMain
from Data.get_data import GetData
from Util.common_util import commonUtil
from Data.dependent_data import dependentData
from Util.send_email import sendEmail
from Util.operation_header import operationHeader
from Util.operation_json import OperationJson

class runTest():
	def __init__(self):
		self.runMain = runMain()
		self.data = GetData()
		self.com_util = commonUtil()
		self.send_mail = sendEmail()

	#程序主入口
	def go_on_run(self):
		res = None
		pass_count = []
		fail_count = []
		rows_count = self.data.get_case_lines()
		for i in range(1,rows_count):
			is_run = self.data.get_is_run(i)
			if is_run:
				url = self.data.get_request_url(i)
				method = self.data.get_request_method(i)
				request_data = self.data.get_data_for_json(i)
				header = self.data.is_header(i)
				depend_case = self.data.is_depend(i)
				expect = self.data.get_expect_for_mysql(i)
				if depend_case != None:
					self.depend_data = dependentData(depend_case)
					#获取的依赖响应数据
					depend_response_data = self.depend_data.get_data_for_key(i)
					#获取依赖的key
					depend_key = self.data.get_depend_field(i)
					# print(depend_key)
					request_data[depend_key] = depend_response_data
				if header == 'write':
					res = self.runMain.run_main(url, method, request_data)
					op_header = operationHeader()
					op_header.write_cookie()

				elif header == 'yes':
					op_json = OperationJson('C:/Users/Administrator/Desktop/interfaceTest/Dataconflg/cooke.json')
					cookie = op_json.get_data('apsid')
					cookies = {
						'apsid':cookie
					}
					res = self.runMain.run_main(url, method, request_data, cookies)
				else:
					res = self.runMain.run_main(url, method, request_data)

				if self.com_util.is_contain(expect, res):
					self.data.write_result(i, 'pass')
					pass_count.append(i)
					# print("测试通过")
				else:
					self.data.write_result(i, res)
					fail_count.append(i)
					# print("测试失败")
				# print(res + '\n'*2)
		self.send_mail.send_main(pass_count,fail_count)


if __name__ == '__main__':
	run = runTest()
	res = run.go_on_run()