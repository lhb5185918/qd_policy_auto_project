import json
from util.mysql_util import Pysql_util


def get_case_data(data):  # 用例data类型取值工具
    if data == "":
        res = data
    elif data != "":
        data = json.loads(data)
        res = data
    return data
