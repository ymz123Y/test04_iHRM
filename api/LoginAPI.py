"""
封装类：
    封装请求函数(只有一个登陆函数)
"""
from app import BASE_URL


class Login:
    # 调用初始化函数，封装：url
    def __init__(self):
        self.login_url = BASE_URL + '/api/sys/login'

    # 编写登陆函数  (不需要获取验证码)
    # 需要传递三个参数 ： session + mobile + password
    # 响应： 响应结果需要返回给调用者
    def login(self, session, mobile, password):
        my_login_data = {
            "mobile": mobile,
            "password": password
        }
        return session.post(self.login_url, json=my_login_data)
