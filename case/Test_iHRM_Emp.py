"""
测试员工模块的增删改查实现
"""
# 1.导包
import unittest
import requests
import logging
import app
from api.EmpAPI import EmpCARD


# 2.创建测试类
class TestEmp(unittest.TestCase):
    # 3.初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCARD()

    # 4.资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5. 测试函数1：增
    # 直接执行该测试用例失败的原因： 1.先执行登录操作， 2.还需要提交银行卡（token）
    # 第一个问题解决：使用测试套件组织测试用例
    # 如何提交银行卡：如何实现关联
    # 核心步骤1：token 的提取
    # 核心步骤2：token 的提交
    def test_add(self):
        # 1. 请求业务
        logging.info('添加员工的日志信息')
        response = self.emp_obj.add(self.session, username="y2000", mobile="19955811238")
        print('增加员工响应结果：', response.json())
        id = response.json().get("data").get("id")
        print("新增员工的id : ", id)
        app.USER_ID = id
        # 2. 断言业务
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 6. 测试函数2：改
    def test_update(self):
        # 1. 请求业务
        logging.info('修改员工的日志信息')
        response = self.emp_obj.update(self.session, app.USER_ID, "yzy2000")
        print('*' * 100)
        print("修改后的员工信息：", response.json())
        # 2. 断言业务
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 7. 测试函数3：查
    def test_get(self):
        logging.info('查询员工的日志信息')
        response = self.emp_obj.get(self.session, app.USER_ID)
        print('*' * 100)
        print("查询到的新员工信息为：", response.json())
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 8. 测试函数4：删
    def test_delete(self):
        logging.info('删除员工的日志信息')
        response = self.emp_obj.delete(self.session, app.USER_ID)
        print('*' * 100)
        print('删除成功后的员工信息：', response.json())
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))


if __name__ == '__main__':
    unittest.main()
