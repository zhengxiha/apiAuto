import sys
import traceback
import json
import pytest
import requests
import allure
from config.global_config import TEST_HOST
from loguru import logger
"""
如果用例执行前需要先登录获取token值，就要用到conftest.py文件了
作用：conftest.py 配置里可以实现数据共享，不需要import导入 conftest.py，pytest用例会自动查找
scope参数为session，那么所有的测试文件执行前执行一次
scope参数为module，那么每一个测试文件执行前都会执行一次conftest文件中的fixture
scope参数为class，那么每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture
scope参数为function，那么所有文件的测试用例执行前都会执行一次conftest文件中的fixture


"""


# 获取到登录请求返回的token值，@pytest.fixture装饰后，testcase文件中直接使用函数名"login_ticket"即可得到token值
@pytest.fixture(scope="session")
def login_ticket():

    header = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    params = {
        "username": "zheng-test",
        "password": "123456",
    }
    # url = 'http://192.168.1.128/api/base-admin/adminUser/login'    #不知哪来的接口
    url = TEST_HOST+'/api/adminUser/login'
    logger.info('开始调用登录接口:{}'.format(url))
    trans_params=json.dumps(params)
    res = requests.post(url, data=trans_params, headers=header, verify=False)  # verify：忽略https的认证
    res=json.loads(res.text)
    try:
        token=res['token']
        # ticket = res.headers['Set-Cookie']
        # logger.info(f"成功获取token-{res['token']}")
        logger.info('登录成功，ticket值为：{}'.format(token))
    except Exception as ex:
        logger.error(f'登录失败！接口返回：{ex}')
    yield token
    print("后置")


# 测试一下conftest.py文件和fixture的作用
@pytest.fixture(scope="session")
def login_test():
    print("运行用例前先登录！")

    # 使用yield关键字实现后置操作，如果上面的前置操作要返回值，在yield后面加上要返回的值
    # 也就是yield既可以实现后置，又可以起到return返回值的作用
    yield "runBeforeTestCase"
    print("运行用例后退出登录！")



# 作用域为类，适用于每个用例执行前后
# 先放着吧 这个好像有点多余
@pytest.fixture(scope="class")
def report_setting():

        # 报告设置
        allure.attach(url,name="请求路径")
        allure.attach(method,name="请求方式")
        allure.attach(json.dumps(res),name="响应数据")