# -*- coding: utf-8 -*-

import requests
import json

class runMain:

    # get请求
    def send_get(self, url, data=None, header=None): 
        res = None
        if header !=None:
            res = requests.get(url=url, data=data,headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        # print(res.status_code)
        return res.json()

    # post请求
    def send_post(self, url, data, header=None):
        res = None
        if header !=None:
            res = requests.post(url=url, data=data,headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        # print(res.status_code)
        return res.json()

    def run_main(self, url, method, data=None, header=None):
        res = None
        if method == 'POST':
            res = self.send_post(url, data, header)
        else:
            res = self.send_get(url, data, header)
        # return json.dumps(res, ensure_ascii = False, sort_keys = True, indent = 2)
        return json.dumps(res, ensure_ascii = False)
