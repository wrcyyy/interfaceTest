# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interfaceTest
@Time    : 2021/3/8 15:52
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : run.py
@IDE     : PyCharm
------------------------------------
"""
import os
import pytest
import sys
from utils.fileoperate import FileOperate


def main():
    allure_features = ['--allure-features']
    allure_features_list = [
        'Login',
    ]
    allure_features_args = ','.join(allure_features_list)
    run_args = allure_features + [allure_features_args]
    # 指定fixture时需要传入run_args参数
    pytest.main(run_args)


if __name__ == '__main__':
    root_dir = os.path.abspath(os.path.dirname(__file__))
    # 指定报告文件路径
    allure_results_dir = os.path.join(root_dir, 'report', 'allure-results')
    FileOperate.create_dirs(allure_results_dir)
    allure_report_dir = os.path.join(root_dir, 'report', 'allure-report')
    FileOperate.create_dirs(allure_report_dir)

    # 执行
    main()
    # 生成报告
    cmd = f'allure generate {allure_results_dir} -o {allure_report_dir} -c'
    print(cmd)
    try:
        os.system(cmd)
    except Exception as e:
        sys.exit()
