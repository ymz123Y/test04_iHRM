"""
封装 unittest 相关实现
"""
# 1.导包
import unittest
import requests
import json
from parameterized import parameterized

import app
from api.LoginAPI import Login


def build_login_data():
    data_list = []
    with open(app.PRO_PATH + '/data/login_data.json', 'r', encoding='utf-8') as f:
        for i in json.load(f).values():
            data_list.append(
                (
                    i.get("mobile"),
                    i.get("password"),
                    i.get("success"),
                    i.get("code"),
                    i.get("message")
                )
            )
    return data_list


# 2.创建测试类（继承 unittest.TestCase）
class TestIHRMLogin(unittest.TestCase):
    # 3.初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.login_obj = Login()
        # 4.资源卸载函数

    def tearDown(self) -> None:
        self.session.close()

    # 5.核心：编写测试登陆函数
    @parameterized.expand(build_login_data())
    def test_login(self, mobile, password, success, code, message):
        # 5-1 参数化
        print('*' * 50)
        print(mobile, password, success, code, message)
        # 5-2 请求业务
        response = self.login_obj.login(self.session, mobile, password)
        print(response.json())
        # 5-3 断言业务
        try:
            self.assertEqual(success, response.json().get("success"))
            self.assertEqual(code, response.json().get("code"))
            self.assertIn(message, response.json().get("message"))
        except Exception as e:
            print('断言的错误为：', e)

    # 编写登陆成功的测试函数
    def test_login_success(self):
        # 1.直接通过提交正向业务，发送请求业务
        response = self.login_obj.login(self.session, '13800000002', '123456')
        print(response.json())
        # 2.断言业务
        # {'success': True, 'code': 10000, 'message': '操作成功！', 'data': 'fa8e53fa-9b2f-47e2-a0da-a3357aeb08c5'}
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        token = response.json().get("data")
        print('登录后响应的token:', token)
        # 想让其他文件调用该 token 值，可以扩大 token 的作用域(将 token 赋值给 app 的一个全局变量)
        app.TOKEN = token


if __name__ == '__main__':
    unittest.main()
