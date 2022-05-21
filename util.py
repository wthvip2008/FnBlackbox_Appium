import json
import yaml
from selenium import webdriver
import appium.webdriver
from base.base_pase import BasePage
import sys
from os.path import dirname, abspath
from config import DATA_YAML, DIR_PATH, HOST

sys.path.insert(0, abspath(__file__))


# 读取yaml文件
def read_yaml(filename):
    with open(file=filename, mode="r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data


def read_json(file_path):
    """
        读取参数化文件
        :param file_path:
        :return:
    """
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


with open(DATA_YAML) as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']


class GetDriver:
    __app_driver = None
    __web_driver = None

    @classmethod
    def get_app_river(cls):
        if cls.__app_driver is None:
            cls.__app_driver = appium.webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
        return cls.__app_driver

    @classmethod
    def get_web_griver(cls):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.get(HOST)
            cls.__web_driver.maximize_window()
        return cls.__web_driver

# class App(BasePage):
#     def start(self):
#         if self.driver is None:
#             # 启动app
#             # 客户端与appium服务器建立连接的代码
#             self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
#             print(desires,"****调试**************************调试******************")
#             # self.driver.implicitly_wait(5)
#             return self.driver
#         else:
#             # 启动应用
#             self.driver.launch_app()
#
#
#     def restart(self):
#         # 重启app
#         self.driver.close_app()
#         self.driver.launch_app()
#
#     def stop(self):
#         # 停止app
#         self.driver.quit()
