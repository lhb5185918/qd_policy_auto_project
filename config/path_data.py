import os
import time
log_time = time.strftime("%Y %D")
log_file_time = "{}_{}_{}.log".format(log_time[0:4],log_time[5:7],log_time[8:10])

local_path = os.path.abspath(__file__)

project_path = os.path.dirname(os.path.dirname(local_path))

config_path = project_path + os.sep + "config"

comm_path = project_path + os.sep + "common"

log_path = project_path + os.sep + "log"

report_path = project_path + os.sep + "report"

test_case_path = project_path + os.sep + "test_case"

util_path = project_path + os.sep + "util"

case_path = project_path+os.sep+"config"+os.sep+"case.xlsx"

log_file_path = project_path+os.sep+"log"+os.sep+log_file_time

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

    @staticmethod
    def get_log_file_path():
        return log_file_path

    def case_path(self):
        return case_path

