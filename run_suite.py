import os
import unittest
from htmltestreport import HTMLTestReport
# import HTMLTestReportCN 网上测试报告

from config import DIR_PATH

suite = unittest.defaultTestLoader.discover("./test_dir")
file_path = DIR_PATH + os.sep + "test_report" + os.sep + "Jenkun_Auto.html"
print(file_path)
HTMLTestReport(file_path).run(suite)
