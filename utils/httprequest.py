# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 14:38
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : httprequest.py
@IDE     : PyCharm
------------------------------------
"""
import logging
import requests


class Request:
    BASE_URL = ''
    VERIFY = False

    def __init__(self, base_url, verify=False):
        self.BASE_URL = base_url
        self.VERIFY = verify

    def send_request(self, method, path, header, params_type='form', data=None, body=None, file_path=None, desc=''):

        """
                封装http请求，根据请求方式及参数类型自动判断使用哪些参数来发送请求
                :param method: 请求方法
                :param path: api路径，需要以/开头，例如`/api/user`
                :param header: 请求头
                :param params_type: 参数类型，用于post请求，参数值：form|json
                :param data: post请求中的参数,当请求消息体为form时，使用此参数
                :param body: post请求中的body，当消息体为json时使用
                :param file_path: 文件路径，用于文件上传
                :param desc: 接口描述
                :return:
                """
        url = f'{self.BASE_URL}{path}'
        params_type = params_type.upper()
        res = None
        try:
            if method.upper() == 'GET':
                res = requests.get(url=url, params=data, headers=header, verify=self.VERIFY)
            elif method.upper() == 'POST':
                res = self.__post(params_type, file_path, url, data, header, body)
            elif method.upper() == 'DELETE':
                res = requests.delete(url, headers=header, params=data, verify=self.VERIFY)
            elif method.upper() == 'PUT':
                if params_type == 'JSON':
                    res = requests.put(url, params=data, json=body, headers=header, verify=self.VERIFY)
                elif params_type == 'form':
                    res = requests.put(url, data=data, headers=header, verify=self.VERIFY)
            res_dicts = {
                'code': res.status_code,
                'text': res.text,
                'time_consuming': res.elapsed.microseconds / 1000,
                'time_total': res.elapsed.total_seconds(),
                'content': res.content
            }
            try:
                res_dicts['body'] = res.json()
            except Exception as e:
                res_dicts['body'] = ''
            logging.info(f"{desc}-[{method.upper()}]:{url} Params:{data} Body:{body} ")
            if 'application/json' in res.headers['Content-Type']:
                logging.info(f"Response:{res_dicts['text']}")
            else:
                logging.info(f"Response:文件相关接口不打印响应信息！,status_code:{res_dicts['code']}")
            return res_dicts
        except requests.RequestException as e:
            logging.error("RequestException url:{},error_info:{}".format(url, e))
            return 0

    def __post(self, params_type, file_path, url, data, header, body):
        if params_type == 'FORM':
            if file_path:
                with open(file_path, 'rb') as f:
                    res = requests.post(url, data=data, files={"file": f}, headers=header, verify=self.VERIFY)
            else:
                res = requests.post(url=url, data=data, headers=header, verify=self.VERIFY)
        elif params_type == 'JSON':
            res = requests.post(url=url, params=data, json=body, headers=header, verify=self.VERIFY)
        else:
            res = requests.post(url=url, headers=header, verify=self.VERIFY)
        return res
