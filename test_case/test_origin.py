import pytest
import json
from util.log_util import logger
from util.mysql_util import Pysql_util
from util.read_case import get_case
from util.request_util import Requests
from config.path_data import case_path
from common.get_data import get_case_data
import time


class Test_origin:
    res = get_case(case_path, '原文政策新增测试用例')
    res1 = get_case(case_path, '编辑测试用例')
    res3 = get_case(case_path, '标签维护接口')
    res2 = get_case(case_path, '原文政策删除测试用例')

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('case', res)
    def test_added(self, case, get_token):  # 新增原文政策测试用例
        header = dict(get_token, **json.loads(case['header']))
        url = case['url']
        data = get_case_data(case['data'])
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        res = Requests().send(url=url, header=header, data=data, method=method)
        logger.info('{}{}{}'.format(number, title, res))
        base_ruesult = Pysql_util().singal_select(
            "select * from p_policy_original_info where policy_title=" + "'" + data['policyTitle'] + "'" + ";")[
            'policy_title']
        assert base_ruesult == data['policyTitle']
        assert res['code'] == 200

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('case', res1)
    def test_update(self, case, get_token):
        header = dict(get_token, **json.loads(case['header']))
        url = case['url']
        data = get_case_data(case['data'])
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        res = Requests().send(url=url, header=header, data=data, method=method)
        logger.info('{}{}{}'.format(number, title, res))
        assert res['code'] == 200

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('case', res3)
    def test_label(self, case, get_token, get_policy_id):
        header = get_token
        url = case['url']
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        for i in get_policy_id:
            data = {"policyId": i['id'], "policyType": "1"}
            time.sleep(30)
            res = Requests().send(url=url, header=header, data=data, method=method)
            logger.info('{}{}{}'.format(number, title, res))
            assert res['code'] == 200

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('case', res2)
    def test_delete(self, case, get_token, get_policy_id):
        header = get_token
        url = case['url']
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        for i in get_policy_id:
            data = {"ids": i['id']}
            if data == None:
                logger.info('政策已删除 {}{}'.format(number, title))
            else:
                res = Requests().send(data=data, header=header, url=url, method=method)
                logger.info('{}{}{}'.format(number, title, res))
                assert res['code'] == 200
