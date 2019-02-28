# coding: utf-8 
import smtplib
from email.mime.text import MIMEText 

class sendEmail:
	global send_user
	global host
	global password
	password = '12002103gx..'
	host = 'smtp.mxhichina.com'
	send_user = 'torres.guan@reiniot.com'
	def send_mail(self, userlist, sub, content):
		user = 'torres'+'<'+send_user+'>'
		message = MIMEText(content, _subtype = 'plain', _charset = 'utf-8')
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ";".join(userlist)
		smpt_sever = smtplib.SMTP()
		smpt_sever.connect(host)
		smpt_sever.login(send_user, password)
		smpt_sever.sendmail(user, userlist, message.as_string())
		smpt_sever.close()

	def send_main(self, pass_list, fail_list):
		pass_num = float(len(pass_list))
		fail_num = float(len(fail_list))
		count_num = pass_num + fail_num
		pass_result = "%.2f%%" %(pass_num/count_num*100)
		fail_result = "%.2f%%" %(fail_num/count_num*100)
		uesrlist = ['gx12002103@163.com']
		sub = '接口自动化测试报告'
		content = '此次一共运行接口个数为%d个，通过个数为%d个，失败个数为%d个，通过率为%s，失败率为%s'%(
			count_num,pass_num,fail_num,pass_result,fail_result)
		self.send_mail(uesrlist, sub, content)


if __name__ == '__main__':
	sen = sendEmail()
	sen.send_main([1,2,3,4],[5,6,7,8,9,10])