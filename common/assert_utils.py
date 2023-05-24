#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2023/2/3 17:36
# @Author : xiha
# @File : assert_utils.py
# @Editor : PyCharm


import json
import re
import pymysql
from loguru import logger
'''
    断言类型：none:默认执行通过 
            json_key: 检查响应数据中是否存在某个键
            json_key_value: 检查响应数据的某个键值对是否与预期相同
            body_regexp: 根据正则表达式断言，能找到check_data的值则算通过
            header_key_check: 检查响应头是否存在某个键
            header_key_value_check: 检查响应头是否存在某个键值对
            response_code_check:状态码断言
            sql_check: 还未完成，预留后面做数据库断言
'''
class CheckUtils():

    def __init__(self, response_data):
    #  def __init__(self, response_data,type,expect):
        """
        :param response_data: 响应结果
        """
        self.response_data = response_data

        self.function = {
            "none": self.none_check(),
            "json_key": self.key_check,
            "json_key_value": self.key_value_check,
            "body_regexp": self.body_regexp_check,
            "header_key_check": self.header_key_check,
            "header_key_value_check": self.header_key_value_check,
            "response_code_check": self.response_code_check,
            "sql_check": self.sql_check
        }

    def none_check(self):
        """
        断言类型为空的情况
        :return:
        """
        return True

    def key_check(self, check_data):
        """
        检查键是否相同
        :param check_data: 需要检查的字段,注意得是字符串才行,因为要分割
        :return: True说明断言成功，False说明断言失败
        """
        # 字符串逗号分割
        key_list = check_data.split(",")
        tmp_result = []
        # 取出需要断言的字段
        for check_key in key_list:
            # 如果 check_key 在json串的键当中，则添加True，不是则添加False
            if check_key in self.response_data.json().keys():
                tmp_result.append(True)
            else:
                tmp_result.append(False)
        if False in tmp_result:
            # 只要有一个不符合 用例全部失败
            return False
        else:
            return True

    def key_value_check(self, check_data):
        """
        检查键值对是否一致
        :param check_data:要传json格式字符串，属性值用双引号，若用单引号会断言异常，没有提示
                        如json用例中要写成--"expect":"{\"code\": \"2000\"}"
        :return:
        """
        key_dict = json.loads(check_data)
        tmp_result = []

        for check_key in key_dict.items():
            if check_key in self.response_data.json().items():
                tmp_result.append(True)
            else:
                tmp_result.append(False)
        if False in tmp_result:
            return False
        else:
            return True

    def body_regexp_check(self, check_data):
        """
        根据正则表达式断言
        :param check_data:要传json格式字符串，属性值用双引号，若用单引号会断言异常，没有提示
                        如json用例中要写成--"expect": "\"msg\":\"(.+?)\""
        :return:
        """
        if re.findall(check_data, self.response_data.text):
            # 能找到check_data的值则算通过
            return True
        else:
            print("正则断言失败")
            return False

    def header_key_check(self, check_data):
        """
        检查头部信息是否包含某个值  可以参照key_check()
        :param check_data:
        :return:
        """
        # 字符串逗号分割
        key_list = check_data.split(",")
        tmp_result = []
        # 取出需要断言的字段
        for check_key in key_list:
            # 如果 check_key 在json串的键当中，则添加True，不是则添加False
            if check_key in self.response_data.headers.keys():
                tmp_result.append(True)
            else:
                tmp_result.append(False)
        if False in tmp_result:
            # 只要有一个不符合 用例全部失败
            return False
        else:
            return True

    def header_key_value_check(self, check_data):
        """
        检查头部键值对是否一致 参照key_value_check()
        :param check_data:
        :return:
        """
        key_dict = json.loads(check_data)
        tmp_result = []

        for check_key in key_dict.items():
            if check_key in self.response_data.headers.items():
                tmp_result.append(True)
            else:
                tmp_result.append(False)
        if False in tmp_result:
            return False
        else:
            return True

    def response_code_check(self, check_data):
        """
        检查返回状态码
        :param check_data:
        :return:
        """
        if self.response_data.status_code == int(check_data):
            return True
        else:
            print("状态码断言失败")
            return False

    def sql_check(self,sql):
        """
        返回某字段数据与数据库数据对比是否一致,未完成
        :param sql:
        """
        db = pymysql.connect(host='',
                             user='',
                             password='',
                             database=''
                             )
        cursor = db.cursor()
        # 执行sql语句获取数据
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            db.rollback()
            print(e)
        finally:
            cursor.close()
            db.close()
        # return result






    # @classmethod
    def run_check(self, check_type, except_result):
        """
        :param check_type: 检查的类型
        :param except_result: 检查的字段
        :return:
        """
        if check_type == "none" or except_result == "":
            logger.info(f"断言类型：{check_type},预期：{except_result}")
            return self.function["none"]
        # 使用return self.function["none"]()会报错
        else:
            logger.info(f"断言类型：{check_type},预期：{except_result}")
            return self.function[check_type](except_result)


if __name__ == '__main__':
    import requests

    url = "https://api.weixin.qq.com/cgi-bin/token"
    get_params = {"grant_type": "client_credential", "appid": "wxb637f897f0bf1f0d",
                  "secret": "501123d2d367b109a5cb9a9011d0f084"}


    response = requests.get(url=url, params=get_params)
    # print(response.headers)

    ck = CheckUtils(response)
    print(ck.none_check())
    print(ck.run_check('', ""))
    print(ck.run_check('none', ""))
    print(ck.run_check('json_key', "access_token,expires_in"))
    print(ck.run_check('json_key_value', '{"expires_in": 7200}'))
    print(ck.run_check("body_regexp", '"access_token":"(.+?)"'))
    print(ck.run_check("header_key_check", "Connection"))
    print(ck.run_check("header_key_value_check", '{"Connection": "keep-alive"}'))
    print(ck.run_check("response_code_check", "200"))
    # print(ck.run_check("sql_check","select employee_id from attendance_log where employee_id=2492 and (attendance_type=1 or attendance_type=4)"))


