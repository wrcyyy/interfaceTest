# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 15:09
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : common_steps.py
@IDE     : PyCharm
------------------------------------
"""
import allure
from os import path
from utils.fileoperate import FileOperate


@allure.step('读取配置文件')
def read_config_file_step(
        info=None,
        config_file_path=path.join(path.dirname(path.dirname(__file__)), 'config', 'config.yml')):
    """
    读取配置文件
    :param info:
    :param config_file_path: 配置文件路径
    :return:
    """
    if info:
        res = FileOperate.read_yaml(config_file_path)[info]
    else:
        res = FileOperate.read_yaml(config_file_path)
    return res
