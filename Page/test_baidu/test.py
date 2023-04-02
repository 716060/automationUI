# -*- coding:utf-8 -*-
# @Time  :2023/3/30 5:10
# @AUTHOR:希耶谢
import json
import os

import xlrd
import yaml


def create_data(path, sheet_name=None):
    abspath = os.path.abspath(path)
    print("abspath====:", abspath)
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
    return data


if __name__ == '__main__':
    print(create_data(r"../../Data/page_data/test_baidu.xlsx", "baidu_translate"))

    # [{'type': 'url', 'name': '', 'selector': '', 'value': 'https://fanyi.baidu.com/'}, {'type': 'input', 'name': 'translate_text', 'selector': 'css selector', 'value': 'textarea#baidu_translate_input'}, {'type': 'button', 'name': 'translate_button', 'selector': 'css selector', 'value': 'a#translate-button'}, {'type': 'input', 'name': 'translate_output', 'selector': 'css selector', 'value': 'p.ordinary-output.target-output'}, {'type': 'button', 'name': 'close', 'selector': 'css selector', 'value': 'span.app-guide-close'}]
    # [{'type': 'url', 'name': '', 'selector': '', 'value': 'https://fanyi.baidu.com/'}, {'type': 'input', 'name': 'translate_text', 'selector': 'css selector', 'value': 'textarea#baidu_translate_input'}, {'type': 'button', 'name': 'translate_button', 'selector': 'css selector', 'value': 'a#translate-button'}, {'type': 'input', 'name': 'translate_output', 'selector': 'css selector', 'value': 'p.ordinary-output.target-output'}, {'type': 'button', 'name': 'close', 'selector': 'css selector', 'value': 'span.app-guide-close'}]
    # [{'type': 'url', 'name': '', 'selector': '', 'value': 'https://fanyi.baidu.com/'}, {'type': 'input', 'name': 'translate_text', 'selector': 'css selector', 'value': 'textarea#baidu_translate_input'}, {'type': 'button', 'name': 'translate_button', 'selector': 'css selector', 'value': 'a#translate-button'}, {'type': 'input', 'name': 'translate_output', 'selector': 'css selector', 'value': 'p.ordinary-output.target-output'}, {'type': 'button', 'name': 'close', 'selector': 'css selector', 'value': 'span.app-guide-close'}]
