import json
import os

'''
    封装读取文件内容
'''


class ReadJsonFileUtils:
    def __init__(self, file_name):
        self.file_name = file_name
        # self.data = self.get_data()
        # self.data=self.get_json_data()

    # 获取json文件中所有的数据--原有获取方式
    def get_json_data(self):
        json_data = []
        with open(self.file_name, 'r', encoding="utf-8") as p:
            for j, r in json.load(p).items():
                r['case_name']=j    #将用例名追加到用例内
                json_data.append(r)
                print("打印json_data:",json_data)
        return json_data

    # 获取json文件数据--现在用这种
    def get_data(self):
        fp = open(self.file_name, encoding='utf-8')
        data = json.load(fp)
        print("打印data:",data)
        fp.close()
        return data

    def get_value(self, id):
        return self.data[id]

    @staticmethod
    def get_data_path(folder, fileName):
        BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        data_file_path = os.path.join(BASE_PATH, folder, fileName)
        return data_file_path


if __name__ == '__main__':
    opers = ReadJsonFileUtils("..\\resources\\test1_data.json").get_data()
    # 读取文件中的dataItem,是一个list列表，list列表中包含多个字典
    # dataitem = opers.get_value('基础设置-店铺管理-新增数据')
    # print(dataitem)
    # jsondata=ReadJsonFileUtils("..\\data\\test1.json").get_json_data()
    jsondata=ReadJsonFileUtils("..\\data\\case_json\\case_data1.json").get_data()