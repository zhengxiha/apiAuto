import requests
import pytest
import json
from common.http_utils import HttpUtils
from config.global_config import TEST_HOST
from utils.read_jsonfile_utils import ReadJsonFileUtils
import allure
from loguru import logger


class TestCase1():

    # 前置login_ticket获取token
    # 用例执行前，先读取准备的数据
    # @pytest.mark.parametrize("data",ReadJsonFileUtils("./data/case_json/case_data.json").get_json_data())
    @pytest.mark.parametrize("data",ReadJsonFileUtils("./data/case_json/case_data.json").get_data())
    @pytest.mark.attendance1
    @allure.title("{data[case_name]}")  # 用例标题
    # @allure.testcase("http://192.168.1.169:8082/testcase-browse-5-0-all-0-pri_asc-55-100.html?tid=c2dhwax6")  #可显示用例管理的链接
    def test_attendance1(self,data,login_ticket):

        # allure报告设置
        # 动态生成标题
        allure.dynamic.title(data['case_name'])
        allure.dynamic.link(TEST_HOST+data['url'])
        # 打印token
        # print("打印token呆:",login_ticket)
        url=TEST_HOST + data['url']
        headers=data['headers']
        method=data['method']

        if method=='post':
            parameters=data['data']
            trans_parameters = json.dumps(parameters)  #将字典转化为字符串
            logger.info(f"执行用例：{data['case_name']}-请求方式：post-请求接口:{url}")

            res=HttpUtils.http_post(headers,url,trans_parameters)
            logger.info(f"响应结果：{res}")


        elif method=='get':
            logger.info(f"执行用例：{data['case_name']}-请求方式:get-请求接口:{url}")
            res=HttpUtils.http_get(headers,url)
            logger.info(f"响应结果：{res}")


        # 报告设置
        allure.attach(url,name="请求路径")
        allure.attach(method,name="请求方式")
        allure.attach(json.dumps(res),name="响应数据")
        assert res['msg']=='成功'



# if __name__ == "__main__":
#     TestCase1().test_attendance1()

