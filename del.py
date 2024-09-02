from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    driver.get('https://entry-demo.dfzxvip.com/index?redirect=https://nuwa-demo.dfzxvip.com/label/labelList')
    driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div[1]/input').send_keys("cuijianwei")
    driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div[2]/input').send_keys("1")
    driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div[4]').click()
    sleep(5)
    # config = driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]')
    # actions = ActionChains(driver)
    # actions.move_to_element(config).perform()
    # driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/span').click()
    # sleep(1)
    # driver.find_element("xpath", '//*[@id="categoryName"]').send_keys("用户测试标签")
    # driver.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span').click()
    # driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/div[5]/div/div[1]').click()
    sdk = driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]')
    sdk_list = sdk.text.split('\n')
    index = sdk_list.index('用户测试标签')
    sdk.find_element("xpath", './div[{}]'.format(index+1)).click()
    sleep(1)
    driver.find_element("xpath", '//*[@id="rc-tabs-0-panel-BASE"]/div/div[1]/div[3]/div[1]/button/span').click()
    sleep(2)

    tbody = driver.find_element("xpath", '/html/body/div[2]/div/div[3]/div/div[2]/div/div[1]/form[2]/div[2]/div[1]/div/div/table/tbody')
    label_num = len(tbody.find_elements("xpath", './tr'))
    selectNum  = 0
    td_len = 0
    div_num = 3
    for num in range(label_num):
        base_tab = driver.find_element("xpath", '/html/body/div[2]/div/div[3]/div/div[2]/div/div[1]/form[2]/div[2]/div[1]/div/div/table/tbody/tr[{}]'.format(num + 1))
        if base_tab.find_element('class name', 'ant-checkbox-input').is_selected():
            pass
        else:
            td_len = len(base_tab.find_elements("xpath", './td'))
            for td in range(4, td_len):
                tab = base_tab.find_element("xpath", './td[{}]'.format(td + 1))
                if td == 4:
                    tab.find_element("class name", 'td-button-small___K3pKn').click()
                    sleep(5)
                    tab.find_element("xpath", '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[1]/div/label/span/input').click()
                    sleep(1)
                    driver.find_element("xpath", '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]/span').click()
                    sleep(1)
                    tab.find_element('class name', 'ant-select-selector').click()
                    sleep(1)
                    tab_value = driver.find_element('xpath', '/html/body/div[{}]'.format(div_num))
                    div_num += 1
                    new_tab = tab_value.find_element('class name', 'rc-virtual-list-holder-inner')
                    new_tab.find_element('xpath', './div[1]').click()
                else:
                    if '选择' in tab.text:
                        tab.click()
                        sleep(1)
                        tab_value = driver.find_element('xpath', '/html/body/div[{}]'.format(div_num))
                        div_num += 1
                        new_tab = tab_value.find_element('class name', 'rc-virtual-list-holder-inner')
                        divs = len(new_tab.find_elements('tag name', 'div'))
                        new_tab.find_element('xpath', './div[{}]'.format(divs // 2)).click()
                        sleep(1)
                    else:
                        pass
            sleep(10)
            break
    driver.close()
