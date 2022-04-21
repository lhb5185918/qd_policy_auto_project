import requests
from util.log_util import logger


class Requests:  # 定义request类
    def api_run(self, url, method, data=None, header=None, cookie=None, file=None, filename=None,
                file_path=None):  # 定义接口输入
        res = None
        # logger.info("请求的url为{}，类型为{}".format(url, type(url)))
        # logger.info("请求的method为{}，类型为{}".format(method, type(method)))
        # logger.info("请求的data为{}，类型为{}".format(data, type(data)))
        # logger.info("请求的header为{}，类型为{}".format(header, type(header)))
        if method == "get":
            res = requests.get(url, data=data, headers=header, cookies=cookie)
        elif method == "post":
            if file != None:
                files = {str(file): (str(filename), open(str(file_path), 'rb'),
                                     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
                res = requests.post(url=url, headers=header, files=files, data=data)
            elif "content-type" not in header:
                res = requests.post(url=url, headers=header, data=data)
            else:
                res = requests.post(url, json=data, headers=header, cookies=cookie)
        code = res.status_code
        cookies = res.cookies.get_dict()
        dict1 = dict()  # 穿件空列表
        try:
            body = res.json()  # 接收返回json格式的响应
        except:
            body = res.text  # 接收返回text格式的响应报文
        dict1['code'] = code
        dict1['body'] = body
        dict1['cookies'] = cookies
        return dict1

    def send(self, url, method, **kwargs):
        return self.api_run(url=url, method=method, **kwargs)
