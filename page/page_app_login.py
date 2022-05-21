from time import sleep

from base.base_pase import BasePage
import page
from nb_logger import logger

class PageAppLogin(BasePage):

    # 输入用户名
    def page_app_input_username(self, value):
        self.base_input(page.app_username, value)

    # 输入验证码
    def page_app_input_message(self, value):
        self.base_input(page.app_message, value)

    # 打钩同意
    def page_app_click_agreement(self):
        self.base_click(page.app_agreement)

    # 点击登录按钮
    def page_app_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 获取操作人姓名
    def page_app_get_nickname(self):
        sleep(2)
        return self.base_get_text(page.app_nickname)

    # 组合业务方法
    def page_app_login(self,username="17718853128",mes='5555'):
        self.page_app_input_username()
        self.page_app_input_message()
        self.page_app_click_agreement()
        self.page_app_click_login_btn()
        self.page_app_get_nickname()