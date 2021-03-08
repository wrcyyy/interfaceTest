# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 14:55
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : Init.py
@IDE     : PyCharm
------------------------------------
"""
from utils.httprequest import Request
from utils.fileoperate import FileOperate
from utils.myassert import Assertions
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
config_info = FileOperate.read_yaml(os.path.abspath(os.path.join(root_dir, 'config', 'config.yml')))['server_conf']
base_url = f"{config_info['protocol']}://{config_info['host']}"

request = Request(base_url, config_info['verify'])


def run_case(yaml_name, index: int, expect=None, token: str = '', param=None, body=None, var: str = None,
             file_path: str = None, params_type: str = 'json'):
    """
    统一的接口调用
    :param yaml_name: params.py文件中的类名
    :param index: 要调用的接口在对应的yaml文件的序列号
    :param expect: 断言，支持str、list、dict类型
    :param token: 令牌，用户登录时获取
    :param param: 参数，用于get请求的参数传入
    :param body: 请求消息体，用于post和put请求的参数传入
    :param var: 用于接口路径中的变量传入，支持str和list类型的参数传入
    :param file_path: 文件路径，用于文件上传时的参数传入
    :param params_type: 用于指定post和put请求消息体格式，支持json和form
    :return:
    """
    total_data = yaml_name()
    path = total_data.url[index]
    data = total_data.data[index]
    header = total_data.header[index]
    bd = total_data.body[index]
    method = total_data.method[index].upper()
    desc = total_data.desc[index]
    header['authorization'] = f'Bearer {token}'
    if param:
        for i in param.keys():
            data[i] = param[i]
    if body:
        if isinstance(body, list):
            bd = body
        elif isinstance(body, dict):
            bd = dict(bd, **body)
    path = make_url(path, var)
    res = request.send_request(method, path, header, params_type=params_type, data=data, body=bd, file_path=file_path,
                               desc=desc)
    if expect:
        expect_assert(expect, res)
    assert Assertions.assert_time(res['time_consuming'], 2000)
    return res


def make_url(path, var):
    """
    对url进行组装
    :param path:
    :param var:
    :return:
    """
    if '$' in path:
        if isinstance(var, str):
            path = path.replace('$', var)
            return path
        elif isinstance(var, list) or isinstance(var, tuple):
            # 当接口路径中有多个变量时循环替换
            for i in var:
                path = path.replace('$', i, 1)
            return path
        else:
            raise ValueError('请传入var参数！')
    else:
        return path


def expect_assert(expect, res):
    """
    对预期进行断言
    :param expect:
    :param res:
    :return:
    """
    if isinstance(expect, list):
        expect_is_list(expect, res)
    elif isinstance(expect, dict):
        expect_is_dict(expect, res)
    elif isinstance(expect, (str, int)):
        assert Assertions.assert_in_text(res['text'], str(expect))
    else:
        raise ValueError('expect参数类型错误，无法断言！')


def expect_is_list(info: list, response):
    """
    断言为列表
    :param info:
    :param response:
    :return:
    """
    for expect_value in info:
        if isinstance(expect_value, (str, int)):
            assert Assertions.assert_in_text(response['text'], str(expect_value))
        elif isinstance(expect_value, dict):
            expect_is_dict(expect_value, response)


def expect_is_dict(info: dict, response):
    """
    断言为字典对象
    :param info:
    :param response:
    :return:
    """
    if 'result' in response['body'].keys():
        for i in info:
            assert Assertions.assert_body(response['body']['result'], i, info[i])
    else:
        for i in info:
            assert Assertions.assert_body(response['body'], i, info[i])
