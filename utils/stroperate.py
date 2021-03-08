# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 15:42
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : stroperate.py
@IDE     : PyCharm
------------------------------------
"""
import hashlib


class String:
    @classmethod
    def transfer_md5(cls, msg: str):
        """
        对字符串进行md5加密
        :param msg:
        :return:
        """
        hl = hashlib.md5(msg.encode('utf-8'))
        return hl.hexdigest().upper()
