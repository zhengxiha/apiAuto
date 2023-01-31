import requests
import json


class HttpUtils:
    '''
    post方法封装
    '''
    @staticmethod
    def http_post(headers, url, parameters):
        """
         post方法封装
        :param headers: 请求头
        :param url: 请求路径
        :param parameters: 请求参数
        :return: 返回响应结果
        """
        res = requests.post(url, data=parameters, headers=headers)  #data格式为json字符串
        # print("接口返回结果：" + res.text)
        test_data=res.text
        if res.status_code != 200:
            raise Exception(u"请求异常")
        result = json.loads(res.text)
        # print("结果：",result)
        return result


    '''
    get方法封装
    '''
    @staticmethod
    def http_get(headers, url):
        """
        get方法封装
        :param headers:
        :param url:
        :return:
        """
        req_headers = json.dumps(headers)
        # print("接口请求url：" + url)
        # print("接口请求headers：" + req_headers)
        res = requests.get(url, headers=headers)
        # print("接口返回结果：" + res.text)
        if res.status_code != 200:
            raise Exception(u"请求异常")
        result = json.loads(res.text)
        return result


    '''
    请求方法封装--优化
    '''
    # def base_requests(self,method,url):
    #     session=requests.Session()
    #     if(file_var in [None])

