# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 16:14
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : conftest.py
@IDE     : PyCharm
------------------------------------
"""
from common.Init import run_case
from TestCase.common_steps import read_config_file_step
from utils.stroperate import String
from api_doc.apis import Login

import pytest


@pytest.fixture(scope='session')
def user_token():
    param = {
        "username": read_config_file_step('server_conf')['username'],
        "password": String.transfer_md5(read_config_file_step('server_conf')['password'])
    }
    token = run_case(Login, 0, ['access_token', 'refresh_token'], param=param, params_type='form')
    yield token['body']['access_token']
    run_case(Login, 1, ['result', 'ok'], token['body']['access_token'])
