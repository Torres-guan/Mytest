# coding: utf-8 
from Util.operation_excel import OperationExcel
from Base.method import runMain
from Data.get_data import GetData
from jsonpath_rw import jsonpath, parse
import json

class dependentData:

	def __init__(self, case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.data = GetData()
		
	#通过case id获取改id的整行数据
	def get_case_line_data(self):
		rows_data = self.opera_excel.get_row_data(self.case_id)
		# print(rows_data)
		return rows_data

	#执行依赖测试，获取结果
	def run_dependent(self):
		run_method = runMain()
		row_num = self.opera_excel.get_row_num(self.case_id)
		request_data = self.data.get_data_for_json(row_num)
		header = self.data.is_header(row_num)
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		res = run_method.run_main(url, method, request_data, header)
		return json.loads(res)

	#根据依赖key去获取执行依赖测试case的响应数据
	def get_data_for_key(self, row):
		depend_data = self.data.get_depend_key(row)
		response_data = self.run_dependent()
		json_exe = parse(depend_data)
		madle = json_exe.find(response_data)
		return [math.value for math in madle][0]

