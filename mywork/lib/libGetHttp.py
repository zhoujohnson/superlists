__author__ = 'Administrator'
#coding=utf8
import urllib
import urllib2
import shutil
from lib import Current_time
from lib import time_diff
from lib import Error_write
from lib import liblog
from conf import config
import httplib
def libGetHttp(interface_name,Base_Add_Url,dict_data):
    #url表示请求的URL,dict_data表示请求的参数的字典模式
    post_data = urllib.urlencode(dict_data)
    #拼接成完整的URL，并将其打印出来
    request_url = Base_Add_Url+"?"+post_data
    print "请求的URL为：",request_url
    #将请求的url拆分出来
    list_url = request_url.split("/")
    list_host_port = list_url[0].split(":")
    req_host = list_host_port[0]
    #print req_host
    req_port = list_host_port[1]
    #print req_port
    req_getUrl = "/"+"/".join(list_url[1:])
    #print req_getUrl

    #定义一个空的列表，用来存放请求时间，返回时间，请求消耗的时间以及返回结果
    array = []

    try:
        #记录接口名称
        name = interface_name
        #将该请求前的系统时间放入列表中
        array.append(name)
        #记录请求前的系统时间
        access_time = Current_time.interval_time()
        #获取系统当前时间
        access_time_now1 = access_time[1]
        #获取系统当前时间戳
        access_time_stamp1 = access_time[0]
        #将该请求前的系统时间放入列表中
        array.append(access_time_now1)
        #调用封装的函数进行get请求
        httpConn = httplib.HTTPConnection(host=req_host,port=req_port)
        httpConn.request("GET",req_getUrl)
        #记录请求后的系统时间
        return_time = Current_time.interval_time()
        #获取系统当前时间
        access_time_now2 = return_time[1]
        #获取系统当前时间戳
        access_time_stamp2 = return_time[0]
        #将该请求后的系统时间放入列表中
        array.append(access_time_now2)
        #计算请求前后的时间差
        cost = time_diff.time_diff(access_time_stamp1,access_time_stamp2)
        #将时间差放入到列表中
        array.append(cost)
        #将服务器返回的数据读取出来，保存到变量content中
        response = httpConn.getresponse()
        content = response.read()
        response_code = response.status
        print "服务器返回的响应码为：",response_code,"，数据为",content
        #将服务器返回的数据放入到列表中
        array.append(content[:800])
        #将返回码放入到列表中
        array.append(response_code)
        #将请求的URL放入到列表中
        array.append(request_url)
        #返回该列表
        return array
    except Exception,ex:
        #将错误信息写入文件中，方便定位问题
        Error_write.error_write(interface_name,request_url,config.Record_file.error_file,ex)

if __name__ == "__main__":
    dict_data = {}
    dict_data["type"] = " "
    dict_data["account"] = 100035
    post_data = urllib.urlencode(dict_data)
    url = "http://qccyb.didihu.com.cn:7060/cyb-app"
    request_url = url + "?" + post_data
    print request_url


