# -*- coding:utf-8 -*-
# @Time  :2023/3/25 22:41
# @AUTHOR:希耶谢
import yaml


# 使用yaml管理用例数据
def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

if __name__ == '__main__':
    print(load_yaml(r"../Data/testcase_data/test_case_01.yaml"))
