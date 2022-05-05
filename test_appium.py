from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
desired_caps = {
    'platformName': 'Android',
    'automationName': "appium",
    'platformVersion': '6.0.1',
    'deviceName': '127.0.0.1:7555',
    'noReset': True,
    'appPackage': 'com.jekunauto.ability.dev',
    'appActivity': 'com.jekunauto.ability.activity.login.LoginActivity',
    'adbExecTimeout': 30000
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
loc_agree = ("id", "com.android.packageinstaller:id/permission_allow_button")
# try:
#     ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@text='允许']")))
#     ele.click()
# except Exception as e:
#     raise e
# else:
#     # loc_permission = ("xpath", "//*[@text='允许']")
#     ele2 = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH,
#     "//*[@text='允许' and @class='android.widget.Button']")))
#     ele2.click()
#     # loc_skip = ("xpath", "//*[@text='跳过']")
#     # ele3 = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(loc_skip))
#     # ele3.click()
#     print("已成功打开集群车宝App.")

# driver.find_element_by_xpath("//*[@text='请输入手机号码']").send_keys(17718853128)
# driver.find_element_by_xpath("//*[@text='请输入手机号码']").send_keys(17718853128)
# driver.find_element_by_xpath("//android.widget.Button[contains(@text='请输入手机号码')]").send_keys(17718853128)
driver.find_element_by_id("com.jekunauto.ability.dev:id/et_phone").send_keys(15814511736)
driver.find_element_by_id("com.jekunauto.ability.dev:id/et_code").send_keys(55555)
driver.find_element_by_id("com.jekunauto.ability.dev:id/iv_privacy_1").click()
button_list=driver.find_elements_by_class_name("android.widget.TextView")

# print(button_list.text)
for button in button_list:
    print(button.text)
driver.find_element_by_id("com.jekunauto.ability.dev:id/tv_login").click()
print("登录成功")
sleep(5)
print(driver.find_element_by_id("com.jekunauto.ability.dev:id/tv_staff_name").text)
sleep(20)
# print(driver.find_element_by_id("com.jekunauto.ability.dev:id/tv_staff_name").text())
driver.quit()
