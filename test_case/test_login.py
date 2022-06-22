import pytest
import json
from util.log_util import logger
from util.mysql_util import Pysql_util
from util.read_case import Case_operation
from util.request_util import Requests
from config.path_data import case_path



class Test_login:
    res = Case_operation().get_case(case_path, '登录测试用例')

    @pytest.mark.parametrize("case", res)
    def test_login(self, case):
        number = case['用例编号']
        title = case['用例名称']
        method = case['method']
        url = case['url']
        header = json.loads(case['header'])
        data = None
        res = Requests().send(url=url, data=data, method=method, header=header)
        Case_operation().write_result(res=title[0:4],xulie=0)
        logger.info("{}{}{},".format(number, title, res))
        assert res['code'] == 200
