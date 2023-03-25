# -*- coding:utf-8 -*-
# @Time  :2023/3/25 22:41
# @AUTHOR:希耶谢
import yaml


# 使用yaml管理用例数据
def load_yaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data
