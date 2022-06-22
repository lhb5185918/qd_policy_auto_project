import pytest
import json
from util.log_util import logger
from util.mysql_util import Pysql_util
from util.read_case import Case_operation
from util.request_util import Requests
from config.path_data import case_path


import time


class Test_origin:
    res = Case_operation().get_case(case_path, '原文政策新增测试用例')
    res1 = Case_operation().get_case(case_path, '编辑测试用例')
    res3 = Case_operation().get_case(case_path, '标签维护接口')
    res2 = Case_operation().get_case(case_path, '原文政策删除测试用例')
    res4 =Case_operation().get_case(case_path,'上传文件接口')


    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('case', res)
    def test_added(self, case, get_token):  # 新增原文政策测试用例
        header = dict(get_token, **json.loads(case['header']))
        url = case['url']
        data = json.loads(case['data'])
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        res = Requests().send(url=url, header=header, data=data, method=method)
        logger.info('{}{}{},'.format(number, title, res))
        time.sleep(1)
        base_ruesult = Pysql_util().singal_select(
            "select * from p_policy_original_info where policy_title=" + "'" + data['policyTitle'] + "'" + ";")[
            'policy_title']
        Case_operation().write_result(res=title[0:4], xulie=2)
        assert base_ruesult == data['policyTitle']
        assert res['code'] == 200


    @pytest.mark.run(order = 2)
    @pytest.mark.parametrize('case',res4)
    def test_put_file(self,case,get_token):#附件上传测试用例
        url =case['url']
        header = get_token
        data = json.loads(case['data'])
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        res =Requests().send(method=method,url = url,data=data,header =header ,file='file',filename = 'case.xlsx',file_path = case_path)
        Case_operation().write_result(res=title[0:4],xulie=6)
        logger.info('{}{}{},'.format(number, title, res))
        assert res['code'] == 200


    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('case', res1)
    def test_update(self, case, get_token):#编辑测试用例
        header = dict(get_token, **json.loads(case['header']))
        url = case['url']
        data = json.loads(case['data'])
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        res = Requests().send(url=url, header=header, data=data, method=method)
        logger.info('{}{}{},'.format(number, title, res))
        Case_operation().write_result(res=title[0:4],xulie=1)
        assert res['code'] == 200

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('case', res3)
    def test_label(self, case, get_token, get_policy_id):
        header = get_token
        url = case['url']
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        for i in get_policy_id:
            data = get_policy_id
            time.sleep(5)
            res = Requests().send(url=url, header=header, data=data, method=method)
            logger.info('{}{}{},'.format(number, title, res))
            Case_operation().write_result(res=title[0:4],xulie=4)
            assert res['code'] == 200


    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('case', res2)
    def test_delete(self, case, get_token, get_policy_id):
        header = get_token
        url = case['url']
        method = case['method']
        title = case['用例名称']
        number = case['用例编号']
        for i in get_policy_id:
            data = {"ids": i['policyId']}
            if data == None:
                logger.info('政策已删除 {}{}'.format(number, title))
            else:
                res = Requests().send(data=data, header=header, url=url, method=method)
                logger.info('{}{}{},'.format(number, title, res))
                Case_operation().write_result(res=title[0:4],xulie=3)
                assert res['code'] == 200