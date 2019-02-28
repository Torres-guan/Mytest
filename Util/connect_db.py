# coding: utf-8
import pymysql
import json

class operationMysql:

	def __init__(self):
		self.db = pymysql.connect(host='192.168.0.10',user='root',passwd='reiniot',
						db='test_case',port=3307,charset='utf8mb4',cursorclass = pymysql.cursors.DictCursor)
		self.cursor = self.db.cursor()

	#查询数据
	def search(self, sql):
		# sql = "select * from user where username='name1'"
		self.cursor.execute(sql)
		result = self.cursor.fetchone()
		return json.dumps(result)
		self.db.close()

if __name__ == '__main__':
	op_mysql = operationMysql()
	a = op_mysql.search("select * from user where username='name1'")
	print(a)