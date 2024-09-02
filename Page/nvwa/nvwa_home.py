from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct
from time import sleep
import allure


@create_data("/Users/koolearn/cuijianwei/pytest-allure-ui/Data/page_data/test_nvwa.xlsx", "nvwa_home")
class Home_page(BrowserAct):
    class Button:
        pass

    class Input:
        pass

    @allure.step("女娲demo登陆界面")
    def open_home(self):
        self.open(self.url)

    @allure.step("进入女娲demo")
    def input_host_pd(self, text):
        self.ele_presence_wait(*self.Input.username).send_keys(text["username"])
        self.ele_presence_wait(*self.Input.passwd).send_keys(text["passwd"])
        self.ele_presence_wait(*self.Input.code).send_keys(text["verificationCode"])
        self.ele_presence_wait(*self.Button.search).click()

        # nvwa_first = self.ele_presence_wait(*self.Button.Assert).text.split("\n")
        # with allure.step("断言结果检查"):
        #     assert len(nvwa_first) > 0, "断言失败信息"

