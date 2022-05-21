from selenium.webdriver.support.wait import WebDriverWait
from nb_logger import logger
from config import IMG_ABS_PATH,IMG_REL_PATH
from appium.webdriver.webdriver import WebDriver

class BasePage:
    # 初始化方法
    def __init__(self, driver: WebDriver = None):
        logger.info("正在初始化, driver对象: {}".format(driver))
        self.driver = driver

    # 查找元素方法
    def base_find(self, loc, timeout=5, poll=0.5):
        logger.info("正在查找元素: {}".format(loc))
        print(1111111111111111111)
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(*loc))

    # 查找元素并点击
    def base_click(self, loc):
        logger.info("正在调用点击元素".format(loc))
        self.base_find(loc).click()

    # 输入元素
    def base_input(self, loc, value):
        logger.info("正在调用输入方法：{} 输入内容是: {}".format(loc, value))
        el = self.base_find(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        logger.info("正在调用获取元素信息方法: {}".format(loc))
        return self.base_find(loc).text

    # 截图方法(绝对路径)
    def base_get_img_abs(self):
        logger.info("正在调用截图方法, 保存位置为{}".format(IMG_ABS_PATH))
        self.driver.get_screenshot_as_file(IMG_ABS_PATH)

    # 截图方法二（相对路径)
    def base_get_img_rel(self):
        logger.info("正在调用截图方法, 保存位置为{}".format(IMG_REL_PATH))
        self.driver.save_screenshot(IMG_REL_PATH)

    # 切换frame
    def base_switch_frame(self, loc):
        logger.info("正在调用切换frame方法, 切换对象: {}".format(loc))
        el = self.base_find(loc)
        self.driver.switch_to.frame(el)

    # 恢复frame
    def base_default_frame(self,loc):
        logger.info("正在调用恢复frame方法, 切换对象: {}".format(loc))
        el = self.base_find(loc)
        self.driver.switch_to.default_content()