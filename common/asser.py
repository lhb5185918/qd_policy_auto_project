class Result:
    def asser(self, code, body):
        if code == 200:
            if body['msg'] == '操作成功':
                result = '接口执行成功'
            elif body['msg'] != '操作成功':
                result = "接口执行失败{}".format(body)
        elif code != 200:
            result = '接口执行失败{}'.format(body)
        return result
