import os
import time

# 根目录
DIR_PATH = os.path.dirname(__file__)
# caps配置文件路径
DATA_YAML = DIR_PATH + os.sep + "datas" + os.sep + "caps.yaml"
# 截图保存位置(绝对路径)
IMG_ABS_PATH = DIR_PATH + os.sep + "img" + os.sep + "{}.png".format(time.strftime("%Y%m%d%H%M%S"))
# 截图保存位置(相对路径)
IMG_REL_PATH = "./img/{}.png".format(time.strftime("%Y%m%d%H%M%S"))
# json测试数据路径
DATA_JSON = DIR_PATH + os.sep + "datas" + os.sep + "data_file.json"
# 集群测试总部后台
HOST = "http://test.fnhq.jekunauto.net/erp/#/headquarters/login"