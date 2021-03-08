# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 14:16
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : test_login.py
@IDE     : PyCharm
------------------------------------
"""
import allure
from api_doc.apis import Login

from common.Init import run_case
from utils.stroperate import String


@allure.feature('Login')
class TestLogin:
    @allure.story('user login')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('正常登录测试')
    @allure.testcase('http://www.baidu.com', '登录测试')
    @allure.issue('http://www.baidu.com', "登录时接口报错")
    def test_user_login(self):
        param = {
            "username": 'wrcyyy@126.com',
            "password": String.transfer_md5('123456')
        }
        run_case(Login, 0, ['access_token', 'refresh_token'], param=param, params_type='form')
