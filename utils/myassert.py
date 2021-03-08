# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 15:02
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : myassert.py
@IDE     : PyCharm
------------------------------------
"""
import logging


class Assertions:

    @classmethod
    def assert_code(cls, code, expected_code):
        """
        断言response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except AssertionError:
            logging.error("statusCode error, expected_code is:{}, statusCode is:{}".format(expected_code, code))
            raise AssertionError

    @classmethod
    def assert_body(cls, body, key, expected_msg):
        try:
            msg = body[key]
            assert msg == expected_msg
            return True
        except AssertionError:
            logging.error(
                "Response body msg != expected_msg, expected_msg is:{}, body_msg is:{}".format(expected_msg, body))
            raise AssertionError

    @classmethod
    def assert_in_text(cls, body, expected_msg):
        """
        断言字符串是否存在
        :param body:
        :param expected_msg:
        :return:
        """
        text = body
        try:
            assert expected_msg in text
            return True
        except AssertionError:
            logging.error(
                "Response body Does not contain expected_msg,  expected_msg is:{}, body_msg is:{}".format(expected_msg,
                                                                                                          text))
            raise AssertionError

    @classmethod
    def assert_not_in_text(cls, body, not_expected_msg):
        """
        断言字符串是否存在
        :param body:
        :param not_expected_msg:
        :return:
        """
        text = body
        try:
            assert not_expected_msg not in text
            return True
        except AssertionError:
            logging.error("Response body has contain not_expected_msg,  not_expected_msg is:{}, body_msg is:{}".format(
                not_expected_msg, text))
            raise AssertionError

    @classmethod
    def assert_text(cls, body, expected_msg):
        """
        断言response中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True
        except AssertionError:
            logging.error("Response body != expected_msg,  expected_msg is:{}, body_msg is:{}".format(expected_msg,
                                                                                                      body))
            raise AssertionError

    @classmethod
    def assert_time(cls, response_time, expected_time=5000):
        """
        断言响应时间是否小于预期时间，单位：ms
        :param response_time: 响应时间
        :param expected_time: 预期时间，默认时间5秒
        :return:
        """
        try:
            assert response_time < expected_time
            return True
        except AssertionError:
            logging.error(
                "Response time > expected_time, expected_time is:{}, response time is:{}".format(expected_time,
                                                                                                 response_time))
            raise AssertionError
