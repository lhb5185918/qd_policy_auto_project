import logging
import os
from config.path_data import Get_path
import time
class Log_util:
    def __init__(self):
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        self.log_name ='{}.log'.format(time.strftime("%Y_%m_%d"))
        self.log_path_file = os.path.join(Get_path.get_log_path(),self.log_name)
        fh = logging.FileHandler(self.log_path_file,encoding='utf-8',mode='w')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        fh.close()
        '''fh_stream = logging.StreamHandler()
        fh_stream.setLevel(logging.DEBUG)
        fh_stream.setFormatter(formatter)
        self.logger.addHandler(fh_stream)'''
    def log(self):
        return self.logger
logger = Log_util().log()