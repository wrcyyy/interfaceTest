# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 14:19
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : apis.py
@IDE     : PyCharm
------------------------------------
"""
import os
import logging
from utils.fileoperate import FileOperate

root_dir = os.path.dirname(os.path.dirname(__file__))


class Base:
    def __init__(self, dir_name, file_name, root_dir_name=os.path.abspath(os.path.join(root_dir, 'api_doc'))):
        self.url, self.method, self.data, self.header, self.body, self.desc = [], [], [], [], [], []
        self.__run(dir_name, root_dir_name, file_name)

    def __run(self, dir_name, root_dir_name, file_name):
        file_path = os.path.abspath(os.path.join(os.path.join(root_dir_name, dir_name), file_name))
        info = FileOperate.read_yaml(file_path)['parameters']
        if info:
            self.url = [x['url'] for x in info]
            self.method = [x['method'] for x in info]
            self.header = [x['header'] for x in info]
            self.data = [x['data'] for x in info]
            self.body = [x['body'] for x in info]
            self.desc = [x['desc'] for x in info]


class Login(Base):
    def __init__(self):
        super(Login, self).__init__('Login', 'Login.yml')


if __name__ == '__main__':
    login_obj = Login()
    print(login_obj.url, login_obj.header)
