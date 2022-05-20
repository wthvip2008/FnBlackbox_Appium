from selenium.webdriver.common.by import By
import config
"""
一、以为下为app登录模块配置信息
"""
# 用户名
app_username = By.ID, "com.jekunauto.ability.dev:id/et_phone"
# 验证码
app_message = By.ID, "com.jekunauto.ability.dev:id/et_code"
# 勾选同意
app_agreement = By.ID, "com.jekunauto.ability.dev:id/iv_privacy_1"
# 登录按钮
app_login_btn = By.ID, "com.jekunauto.ability.dev:id/tv_login"
# 登录人姓名
app_nickname = By.ID, "com.jekunauto.ability.dev:id/tv_staff_name"
