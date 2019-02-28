# -*- coding: utf-8 -*-

import unittest
from method import runMain
import HTMLTestRunner
from mock import mock
from mock_interface import mock_test


class testMethod(unittest.TestCase):

    # 执行测试之前执行
    @classmethod
    def setUpClass(cls):
        pass

    # 执行测试之后执行
    @classmethod
    def tearDownClass(cls):
        pass

    # 每条测试用例执行之前执行
    def setUp(self):
        self.run = runMain()

    # 每条测试用例测试执行之后执行
    def tearDown(self):
        pass

    # 测试用例
    def test_01(self):
        url = 'https://reiniot.com/api/device/config'
        data = {'imei': '92515277479453',
                'signature': 'ff5aaccea9e7c00d46cdee6652c97460',
                'timestamp': '1544751774'
                }
        # \self.run.run_main = mock.Mock(return_value=data)
        result = mock_test(self.run.run_main, url, "POST", data, data)
        # result = self.run.run_main(url, 'POST', data)
        print(result)
        # self.assertEqual(result['live_br'], 800, "测试失败")

    @unittest.skip('test_02')
    def test_02(self):
        url = 'https://reiniot.com/api/device/config'
        data = {'imei': '92515277479454',
                'signature': 'ff5aaccea9e7c00d46cdee6652c97461',
                'timestamp': '1544751775'
                }
        result = self.run.run_main(url, 'POST', data)
        self.assertEqual(result['status_code'], 443, "测试失败")

if __name__ == '__main__':
    # filepath = "../Report/Report.html"
    # ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(testMethod('test_01'))
    suite.addTest(testMethod('test_02'))
    # runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title="测试报告")
    # runner.run(suite)
    unittest.TextTestRunner().run(suite)
