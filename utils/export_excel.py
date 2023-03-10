#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2023/2/28 10:26
# @Author : xiha
# @File : export_excel.py
# @Editor : PyCharm
import ast
import jsonpath
# from common.my_mysql import My_mysql
# from common.py_log import LoggerHandler

# loger = LoggerHandler()

class MyAssert:
    def assert_db(self,check_db_str):
        """
        1、将check_db_str转成python对象(列表)，通过eval
        2、遍历1中的列表，访问每一组db比对
        3、对于每一组来讲，1）调用数据库类，执行sql语句。调哪个方法，根据type来决定。得到实际结果
                       2）与期望结果比对
        :param check_db_str: 测试数据excel当中，assert_db列读取出来的数据库检验字符串。
              示例：[{"sql":"select id from member where mobile_phone='#phone#'","expected":1,"type":"count"}]
        :return:
        """
		# 所有断言的比对结果列表
        check_db_res = []

        # 把字符串转换成python列表
        check_db_list = ast.literal_eval(check_db_str)  # 比eval安全一点。转成列表。

        # 建立数据库连接
        db = My_mysql()

        # 遍历check_db_list
        for check_db_dict in check_db_list:
            loger.info("当前要比对的sql语句：\n{}".format(check_db_dict["sql"]))
            loger.info("当前执行sql的查询类型（查询结果条数 或 查询某个值。）：\n{}".format(check_db_dict["db_type"]))
            loger.info("期望结果为：\n{}".format(check_db_dict["expected"]))

            # 根据type来调用不同的方法来执行sql语句。
            if check_db_dict["db_type"] == "count":
                 loger.info("比对数据库查询的结果条数，是否符合期望")

                 # 执行 sql 语句
                 res = db.get_count(check_db_dict["sql"])
                 loger.info("sql的执行结果为：\n{}".format(res))

                 # 将比对结果添加到结果列表当中
                 check_db_res.append(res == check_db_dict["expected"])


                 # if check_db_dict["comp_type"] == "eql":
                 #     check_db_res.append(res == check_db_dict["expected"])

            if False in check_db_res:
                loger.error("部分断言失败！，请查看数据库比对结果为False的")
                # raise AssertionError
                return False
            else:
                loger.info("所有断言成功！")
                return True

if __name__ == '__main__':
    # 已经从excel当中读取出来的字符串
    check_db_str='''[{"sql":"select id from member where mobile_phone='14560748362'","expected":1,"db_type":"count"}]'''
    res = MyAssert().assert_db(check_db_str)
    print(res)

