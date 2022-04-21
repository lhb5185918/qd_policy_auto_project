import os

local_path = os.path.abspath(__file__)

project_path = os.path.dirname(os.path.dirname(local_path))

config_path = project_path + os.sep + "config"

comm_path = project_path + os.sep + "common"

log_path = project_path + os.sep + "log"

report_path = project_path + os.sep + "report"

test_case_path = project_path + os.sep + "test_case"

util_path = project_path + os.sep + "util"

case_path = project_path+os.sep+"config"+os.sep+"case.xlsx"

class Get_path:
    @staticmethod
    def get_common():
        return comm_path

    @staticmethod
    def get_config():
        return config_path

    @staticmethod
    def get_log_path():
        return log_path

    @staticmethod
    def get_report_path():
        return report_path

    @staticmethod
    def get_test_case_path():
        return test_case_path

    @staticmethod
    def get_util_path():
        return util_path

    def case_path(self):
        return case_path

