# -*- coding:utf-8 -*-
# @Time  :2023/3/24 2:40
# @AUTHOR:希耶谢

import os
import json
import yaml
import xlrd

'''
类装饰器，将分离出来的POM页面元素加载进page对象中
excel、yaml、json格式
'''


def create_data(path, sheet_name=None):
    abspath = os.path.abspath(path)
    if not os.path.exists(abspath):
        raise FileNotFoundError("{}文件路径不存在！".format(abspath))
    _is_yaml_file = abspath.endswith((".yml", ".yaml"))
    _is_excel_file = abspath.endswith((".xls", ".xlsx"))
    if _is_yaml_file:
        with open(abspath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    elif _is_excel_file and sheet_name:
        excel_obj = xlrd.open_workbook(abspath)
        sheet_obj = excel_obj.sheet_by_name(sheet_name)
        rows = sheet_obj.nrows
        cols = sheet_obj.ncols
        keys = sheet_obj.row_values(0)
        data = []
        for i in range(1, rows):
            values = sheet_obj.row_values(i)
            data.append(dict(zip(keys, values)))
    else:
        with open(abspath, "r", encoding="utf-8") as f:
            data = json.load(f)

    def wrapper(cls):
        for i in data:
            if i["type"] == "button":
                setattr(getattr(cls, "Button"), i["name"], (i["selector"], i["value"]))
            if i["type"] == "input":
                setattr(getattr(cls, "Input"), i["name"], (i["selector"], i["value"]))
            if i["type"] == "url":
                setattr(cls, "url", i["value"])
            if i["type"] == "frame":
                setattr(cls, "iframe", i["value"])
        return cls

    return wrapper
