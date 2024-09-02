import yaml


# 使用yaml管理测试用例数据
def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

if __name__ == '__main__':
    print(load_yaml(r"../Data/testcase_data/nvwa.yaml")['username'])
