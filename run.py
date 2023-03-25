# -*- coding:utf-8 -*-
# @Time  :2023/3/25 23:30
# @AUTHOR:希耶谢
import os
import pytest


def run():
    pytest.main(['-vs', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')


if __name__ == '__main__':
    run()
