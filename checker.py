#モジュール
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import config

'''
#モードと時間を選択
print('何日の分を入力しますか？\n1: 今日\n2: 昨日\n3: 両方')
category = int(input('番号を入力してください: '))
'''

#日本大学学生健康観察記録システム
website = 'https://condition.nihon-u.ac.jp/Student/Input'

#Chromeの設定・起動
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless') #バックグラウンド実行
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)
driver.maximize_window()

def login():
    #生徒台帳番号入力
    driver.find_element_by_id("No_Member_1").send_keys(config.NU_Number)
    #生年月日入力
    driver.find_element_by_id("Birthday_String").send_keys(config.Birthday)

    driver.find_element_by_name("NoLogin").click()
    driver.find_element_by_class_name("circle").click()
    driver.find_element_by_class_name("btn.btn-success").click()

def check():
    Select(driver.find_element_by_name("Ent_Input.Temperature_1_Time")).select_by_visible_text('1時～')
    driver.find_element_by_id("Ent_Input_Temperature_1_String").clear()
    driver.find_element_by_id("Ent_Input_Temperature_1_String").send_keys(str(round(random.uniform(36.5, 36.9), 1)))
    Select(driver.find_element_by_name("Ent_Input.Temperature_2_Time")).select_by_visible_text('12時～')
    driver.find_element_by_id("Ent_Input_Temperature_2_String").clear()
    driver.find_element_by_id("Ent_Input_Temperature_2_String").send_keys(str(round(random.uniform(36.5, 36.9), 1)))
    for i in range(12):
        i += 1
        driver.find_element_by_id("Check_{0}_N".format(i)).click()
    driver.find_element_by_class_name("btnRegist.btn.btn-primary").click()
    Alert(driver).accept()

login()
check()

