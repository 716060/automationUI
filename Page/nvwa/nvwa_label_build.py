from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct
from time import sleep
import allure


@create_data("/Users/koolearn/cuijianwei/pytest-allure-ui/Data/page_data/test_nvwa.xlsx", "nvwa_label_build")
class Lable_build(BrowserAct):
    class Button:
        pass

    class Input:
        pass

    #步骤1：点击用户测试标签
    def click_user_test_label(self):
        sdk = self.ele_presence_wait(*self.Button.userTestLab)
        index = sdk.text.split('\n').index('用户测试标签')
        self.ele_value_wait_by_sleep(*self.Button.userIndex, sdk, index + 1).click()


    #步骤2：点击新建基础标签
    def click_new_basic_label(self):
        self.ele_presence_wait(*self.Button.buildBaseTab).click()


    #步骤3：定位选择表格，获取表格行数
    def positioning_options_table(self):
        tbody = self.ele_presence_wait(*self.Button.putTab)
        label_num = len(self.eles_value_wait_by_sleep(*self.Button.putTabList, tbody))
        return label_num

    #定位行
    def positioning_rows(self, num):
        return self.ele_presence_wait(*self.Button.lineTab, num)

    #步骤4：遍历每行，直至未被选择的行
    def unselected_rows(self):
        label_num = self.positioning_options_table()
        for num in range(label_num):
            base_tab = self.positioning_rows(num + 1)
            if not self.ele_value_wait_by_sleep(*self.Button.selected, base_tab).is_selected():
                return base_tab

        return -1

    #步骤5:获取列数
    def get_columns(self, base_tab):
        return len(self.eles_value_wait_by_sleep(*self.Button.line, base_tab))

    #定位列值
    def positioning_column(self, cursor, num):
        return self.ele_value_wait_by_sleep(*self.Button.lineInfo, cursor, num)

    #步骤6:点击标签值-采集
    def click_to_collect(self, cursor, div_num):
        self.ele_value_wait_by_sleep(*self.Button.collection, cursor).click()
        sleep(5)
        new_div = self.ele_presence_wait(*self.Button.newDiv, div_num)
        new_div_1 = self.ele_value_wait_by_sleep(*self.Button.selectAll, new_div)
        sleep(1)
        self.ele_value_wait_by_sleep(*self.Button.selectAll_1, new_div_1).click()
        confirm = self.ele_presence_wait(*self.Button.chickConfirm)
        self.ele_value_wait_by_sleep(*self.Button.chickConfirm_2, confirm).click()
        sleep(1)

    #步骤7:下拉菜单点击取值
    def get_values(self, cursor, div_num, data):
        lists = data['selected']
        self.ele_value_wait_by_sleep(*self.Input.tabValue, cursor).click()
        sleep(1)
        tab_value = self.ele_presence_wait(*self.Button.newDiv, div_num)
        new_tab = self.ele_value_wait_by_sleep(*self.Button.elementSelect, tab_value)
        selects = new_tab.text.split('\n')
        div = -1
        for i in range(len(lists)):
            if lists[i] in selects:
                div = selects.index(lists[i])
                break
        if div == -1:
            self.ele_value_wait_by_sleep(*self.Button.selectLast, new_tab, 1).click()
        else:
            self.ele_value_wait_by_sleep(*self.Button.selectLast, new_tab, div + 1).click()

    #步骤8：选中并点击提交
    def confirm(self, cursor):
        first = self.ele_value_wait_by_sleep(*self.Button.lineInfo, cursor, 1)
        self.ele_value_wait_by_sleep(*self.Button.selectAll_1, first).click()
        self.ele_presence_wait(*self.Button.post).click()


    @allure.step("新建基础标签")
    def build_new_label(self, data):

        '''
        在用户测试标签内新建标签
        :return:NULL
        '''

        self.click_user_test_label()
        self.click_new_basic_label()
        div_num = 3
        rowInfo = self.unselected_rows()
        if rowInfo == -1:
            print("所有标签已全部被选中，请更换数据集")
        else:
            base_tab = rowInfo

            columns = self.get_columns(base_tab)
            for column in range(4, columns):
                tab = self.positioning_column(base_tab, column + 1)
                if '采集' in tab.text:
                    self.click_to_collect(tab, div_num)

                if '选择' in tab.text or '输入' in tab.text:
                    self.get_values(tab, div_num, data)
                    div_num += 1

            self.confirm(base_tab)

