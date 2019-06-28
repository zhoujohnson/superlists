__author__ = 'Administrator'
#coding=utf8
from lib import Current_time
from conf import config
def error_write(interface_name,request_url,fileName,content):
    #定义分隔符，后面通过该分隔符进行参数还原
    delimiter = config.Division.division
    file_open = file(fileName,"a+")
    file_open.write(str(interface_name)+delimiter+str(request_url)+delimiter+str(Current_time.interval_time())+delimiter+str(content)+"\n")
    file_open.close()
