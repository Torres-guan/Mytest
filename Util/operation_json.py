# -*- coding: utf-8 -*-
import json

class OperationJson:

    def __init__(self, file_path = None):
        if file_path == None:
            self.file_path = '/var/lib/jenkins/workspace/test/Dataconflg/data.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]

    #写JSON
    def write_data(self, data):
        with open('/var/lib/jenkins/workspace/test/Dataconflg/cooke.json', 'w') as fp:
            fp.write(json.dumps(data))
        

if __name__ == '__main__':
    op = OperationJson()
    print(op.get_data('shebei'))
