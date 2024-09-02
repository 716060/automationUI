from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct
from time import sleep
import allure


@create_data("/Users/koolearn/cuijianwei/pytest-allure-ui/Data/page_data/test_nvwa.xlsx", "user_grouping_list")
class New_Audience(BrowserAct):
    class Button:
        pass

    class Input:
        pass

    @allure.step("新建人群")
    def new_audience(self, text):
        '''

        :param text: 输入人群名称、人群定义以及更新方式
        :return:
        '''
        self.ele_value_normal(*self.Button.group).click()
        self.ele_value_normal(*self.Button.newAudience).click()

        self.ele_value_normal(*self.Input.populationName).send_keys(text["newAudience"]["populationName"])
        self.ele_value_normal(*self.Input.populationDefinition).send_keys(text["newAudience"]["populationDefinition"])
        self.ele_value_normal(*self.Button.update).click()

        self.ele_value_normal(*self.Button.gender).click()

        gender = self.eles_presence_wait(*self.Button.option)
        options = len(gender)
        for i in range(options):
            self.ele_value_wait_by_sleep(self.Button.option_n, gender, i + 1).click()


