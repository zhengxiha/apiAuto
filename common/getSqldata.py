import pymysql
import operator
import logger
import loguru

class SqlAsserts():
    # def assert_fun(self, sql,res_data):
    #     self.sql = sql
    #     self.res_data=res_data
    #     sql_data=self.getSqlData(sql)
    #     assert_data=self.judge_same(sql_data,res_data)
    #     return assert_data

    def getSqlData(self,sql):
        """
        执行sql语句，返回数据类型为元组
        :return:
        """
        # 连接数据库
        db = pymysql.connect(host='',
                             user='',
                             password='',
                             database=''
                             )
        cursor = db.cursor()
        # 表名
        table_name = ''

        # sql = 'select employee_id from %s where employee_id=2492 ' \
        #       'and (attendance_type=1 or attendance_type=4)' % table_name
        # sql = 'select distinct employee_id from %s where employee_id=2492' % table_name

        try:
            result1 = cursor.execute(sql)
            result2 = cursor.fetchall()

        except Exception as e:
            db.rollback()
            print(e)
        finally:
            cursor.close()
            db.close()

        return result2
# res=sqlAssert().getSqlData()
# print("---打印---",res)


    # 判断是否相同
    # def judge_same(self,sql_data,res_data):
    def judge_same(self,sql,res_data):
        sql_data=self.getSqlData(sql)



        global is_same
        sql_data_item=[]
        # sql_data=self.getSqlData()
        # 响应数据提取的字段传过来是字典，operator.eq()内的两个数据需为一种类型
        try:
            if len(sql_data)==len(res_data):
                for a in  sql_data:    #遍历取出元组中的数据，当前只实现最小元组内只有一个数据，所以写sql语句时只能取出一列
                    sql_data_item.append(a[0])  #取出嵌套元组中的第一个元组 sql返回形式是（（x,）（x,））
                print("   查询结果：",sql_data_item)
                print("接口返回结果：",res_data)
                is_same=operator.eq(sql_data_item,res_data)
            else:
                # logger.info("数据库数据与返回数据长度不符")
                print("数据库数据与返回数据长度不符")
                is_same=False
            return is_same
        except Exception as e:
            print(e)



# a=(123,78)
# # b=(123,78)
# b={123,718}
# a=SqlAsserts().getSqlData('select employee_id from attendance_log where employee_id=2492 and (attendance_type=1 or attendance_type=4)')
b=[2492,2492]
x=SqlAsserts().judge_same('select employee_id from attendance_log where employee_id=2492 and (attendance_type=1 or attendance_type=4)',b)
print("断言结果：",x)
#