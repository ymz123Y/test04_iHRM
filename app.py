"""
框架搭建：
    核心： api + case +data
        1)api：封装请求业务（requests）
        2)case:集成 unittest 实现，调用 api 以及参数化解析 data
        3)data :封装测试数据
    测试报告：report + tools + run_suite
        1）report：保存测试报告
        2）tools：封装工具文件
        3）run_suite：组织测试套件
    配置 : app.py
        1）app.py ：封装程序常量以及配置信息
    日志： log
        1）log :保存日志文件

app.py 封装数据
"""
import os
import logging
import logging.handlers

# 封装接口的URL数据
BASE_URL = 'http://182.92.81.159'

# 封装项目路径
# 1. 获取 app.py 文件的绝对路径
APP_PATH = os.path.abspath(__file__)
# 2. 获取 app.py 绝对路径的父级路径(项目路径)
PRO_PATH = os.path.dirname(APP_PATH)

# 定义一个变量
TOKEN = None
USER_ID = None


# 编写日志文件
def my_log_config():
    # 1. 获取日志对象
    logger = logging.getLogger()
    # 2.为日志输出日志级别
    logger.setLevel(logging.INFO)
    # 3.设置日志的输出目标（多目标）
    to_1 = logging.StreamHandler()  # 默认到控制台
    to_2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + '/log/mylog.log',
                                                     when='h',
                                                     interval=12,  # 每12小时产生一个日志文件
                                                     backupCount=10,  # 保留的文件个数
                                                     encoding='utf-8')
    # 4.指定输出格式
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 5.组合要将输出格式与输出目标和日志对象相组合
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    # 将日志的输出目标添加进日志对象
    # 然后输出的时候就会把日志按照指定的格式和指定输出的地方输出出来
    logger.addHandler(to_1)
    logger.addHandler(to_2)



# 调用，在需要的位置调用日志输出
