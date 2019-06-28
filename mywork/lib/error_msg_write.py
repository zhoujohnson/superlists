#coding=utf8
import os
import csv
import time
import os
from lib import Interval_time
from lib import libdatabase
from lib import Interval_time
from lib import Error_write
from lib import liblog
from conf import config
def error_msg_write(error_file,csv_file):
    #先判断该error_file是否存在，若存在，则令成功标志位置为0
    if os.path.exists(error_file):
        flag = 0
        #打开csv_file文件
        csv_file = file(csv_file,"a+")
        writer = csv.writer(csv_file)
        #打开error_file文件
        fileName = file(error_file,"r+")
        #打开Error_msg_backup.txt，将所有异常日志都写在里面
        fileName1 = file(config.Record_file.error_total_file,"a+")
        #将error_file文件中的所有数据都读取出来
        error_msg_list = fileName.readlines()
        #关闭error_file文件，释放资源
        fileName.close()
        #将异常日志都写入到Error_msg_backup.txt文件中，方便以后跟踪
        for line in error_msg_list:
            fileName1.write(line)
        #关闭Error_msg_backup.txt文件，释放资源
        fileName1.close()
        #将error_file中第一行异常日志提取出来，因为该日志是发生错误的根源
        error_msg = error_msg_list[0]
        print error_msg
        #通过之前在Error_write中定义的分隔符还原异常日志中的数据
        first_list = error_msg.split(config.Division.division)
        #接口名称
        interface_name = first_list[0]
        #请求的URL
        request_url = first_list[1]
        #当前系统时间
        error_time = first_list[2]
        #错误日志内容
        error_msg = first_list[3]
        list_error = []
        list_error.append(str(interface_name))
        list_error.append(str(error_time))
        list_error.append("0000-00-00 00:00:00")
        list_error.append("-1")
        list_error.append(str(error_msg))
        list_error.append(str(flag))
        list_error.append("null")
        list_error.append(str(request_url))
        writer.writerow(list_error)
        csv_file.close()
        os.remove(error_file)

    else:
        pass