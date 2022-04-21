import json
from config.path_data import case_path
import pytest
import requests
from util.request_util import Requests
from util.mysql_util import Pysql_util
from util.read_case import get_case


@pytest.fixture(scope="function")
def get_token():  # 获取token的前置脚本
    url = 'https://xha.lingxitest.com/api/lx-operation/lingxi-auth/oauth/token?tenantId=000000&username=gaoxinjishu&password=be85a89ae3d55da3d7a0bba4666e8be3&grant_type=password&scope=all&type=account'
    data = None
    header = {"authorization": "Basic bHhfb3BlcmF0aW9uOmx4X29wZXJhdGlvbl9zZWNyZXQ=",
              "content_type": "application/json;charset=UTF-8"}
    res = requests.post(url=url, data=data, headers=header)
    dict1 = dict()
    res1 = res.json()['access_token']
    dict1['lingxi-auth'] = res1
    dict1['authorization'] = "Basic bHhfb3BlcmF0aW9uOmx4X29wZXJhdGlvbl9zZWNyZXQ="
    return dict1


@pytest.fixture(scope="function")
def get_policy_id():
    res = get_case(case_path, '原文政策新增测试用例')
    result = []
    for i in res:
        id = json.loads(i['data'])['policyTitle']
        sql = "select id from p_policy_original_info where policy_title =" + "'" + id + "'" + "and is_deleted = 0;"
        res1 = Pysql_util().singal_select(sql=sql)
        result.append(res1)
    return result
