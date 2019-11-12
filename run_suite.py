"""
测试套件：
    按照需求组合被执行的测试函数


自动化测试执行顺序：
    增 ----》改 ------》 查 -----》 删

补充说明：
    关于测试套件的组织，接口业务测试中，需要保证测试套件中接口的执行顺序
    合法实现： suite.addTest（类名（“函数名”）） 逐一添加
    非法实现：suite.addTest(unittest.makeSuite(类名)) 虽然可以一次性添加多个测试函数，但是无法保证执行顺序
"""
# 1.导包
import unittest
import time
import app
from case.TestIHRM_Login import TestIHRMLogin
from case.Test_iHRM_Emp import TestEmp

# 2.实例化测试套件对象， 组织被执行的测试函数
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestIHRMLogin("test_login_success"))  # 组织登录成功的测试函数
suite.addTest(TestEmp("test_add"))  # 组织员工新增的测试函数
suite.addTest(TestEmp("test_update"))
suite.addTest(TestEmp("test_get"))
suite.addTest(TestEmp("test_delete"))

# 3.执行套件，生成测试报告
# runner = unittest.TextTestRunner()
# runner.run(suite)
with open(app.PRO_PATH + '/report/report.html', 'wb') as f:
    runner = HTMLTestRunner(f, title="我的测试报告", description="测试iHRM接口")
    runner.run(suite)
