# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 14:21
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : fileoperate.py
@IDE     : PyCharm
------------------------------------
"""
import os
import yaml
import logging


class FileOperate:

    @classmethod
    def read_yaml(cls, file):
        """
        读取yml文件
        :param file:
        :return:
        """
        if os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        else:
            logging.error('文件不存在！{}'.format(file))
            return None

    @classmethod
    def create_dirs(cls, file_dir):
        """
        创建文件路径,先判断目录是否存在
        :param file_dir:
        :return:
        """
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
