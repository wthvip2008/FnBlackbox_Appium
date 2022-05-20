import unittest,config
from parameterized import parameterized
from util import App,read_json
from config import DATA_JSON
from page.page_app_login import PageAppLogin
from nb_logger import logger

class TestAppLoginOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App().start()
        print("```````````````````````````````````````````````",self.app)

    def tearDown(self) -> None:
        self.app.stop()

    # @parameterized.expand(read_json(DATA_JSON))
    @parameterized.expand([("17718853128","55555","李晓杰")])
    def test01_login_order(self, search_value, mes,expect_text):
        try:
            self.app.page_app_input_username(search_value)
            print('111111111111111111111')
            self.app.page_app_input_message(mes)
            self.app.page_app_click_agreement()
            self.app.page_app_click_login_btn()
            nickname = self.app.page_app_get_nickname()
            print("登录账户昵称为：",nickname)
            self.assertEqual(expect_text, nickname)
            logger.info("===>验证成功")
        except Exception as e:
            logger.error(e)
            self.app.base_get_img_abs()
            raise
