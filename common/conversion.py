import json
from util.read_case import get_case
from config.path_data import Get_path

res5 = get_case(Get_path().case_path(), '登录测试用例')


class Conversion:  # 字符串转化字典工具
    def dict_conversion(self, put, key=None):
        if isinstance(put, str):
            res = json.loads(put)
        elif isinstance(put, list):
            for i in put:
                if isinstance(i, dict):
                    res = i
                elif isinstance(i, str):
                    if key == None:
                        print("请输入键值")
                    elif key != None:
                        res = dict(zip(key, put))
                else:
                    res = print("数据类型非字典、列表、字符串类型")
        else:
            res = print("数据类型非列表、字符串类型")
        return res



