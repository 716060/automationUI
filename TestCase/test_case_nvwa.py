import allure
import pytest
from Page.nvwa.nvwa_home import Home_page
from Page.nvwa.nvwa_label_list import Lable_page
from Page.nvwa.nvwa_label_build import Lable_build
from Data_Load.case_data import load_yaml
from time import sleep
from Page.nvwa.nvwa_new_audience import New_Audience


@allure.title("打开并进入女娲首页")
@allure.story("典型场景")
@allure.severity("critical")
@pytest.mark.parametrize('data', load_yaml(r"/Users/koolearn/cuijianwei/pytest-allure-ui/Data/testcase_data/nvwa.yaml"))
def test_01(browser, data):  # browser是conftest中fixture传过来的浏览器对象===一些前置 后置处理
    """
        01 打开女娲登陆界面
        02 输入账号密码登陆
        03 创建新标签列表
    """
    home = Home_page(browser)
    home.open_home()  # 女娲的登陆界面
    home.input_host_pd(data)
    sleep(2)

@allure.title("新建标签列表")
@allure.story("典型场景")
@allure.severity("critical")
@pytest.mark.skip(reason="无理由不想执行")
def test_02(browser):
    Label_list = Lable_page(browser)
    Label_list.build_new_label_list()
    sleep(3)

@allure.title("新建基础标签")
@allure.story("典型场景")
@allure.severity("critical")
@pytest.mark.parametrize('data', load_yaml(r"/Users/koolearn/cuijianwei/pytest-allure-ui/Data/testcase_data/nvwa.yaml"))
@pytest.mark.skip(reason="无理由不想执行")
def test_03(browser, data):
    labelBuild = Lable_build(browser)
    labelBuild.build_new_label(data)
    sleep(3)

@allure.title("新建人群")
@allure.story("典型场景")
@allure.severity("critical")
@pytest.mark.parametrize('data', load_yaml(r"/Users/koolearn/cuijianwei/pytest-allure-ui/Data/testcase_data/nvwa.yaml"))
def test_04(browser, data):
    labelBuild = New_Audience(browser)
    labelBuild.new_audience(data)
    sleep(3)
