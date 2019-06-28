#!/bin/env python
#coding=utf-8
import os

#配置邮件信息
class MailInfo():
        authInfo = {}
        authInfo['server'] = 'smtp.didihu.com.cn'
        authInfo['user'] = 'houcp@didihu.com.cn'
        authInfo['password'] = 'thisisglsx123'
        #添加多个邮箱地址，中间以逗号（，）隔开
        fromAdd = 'houcp@didihu.com.cn'
        toAdd = "houcp@didihu.com.cn"
        ccAdd = "houcp@didihu.com.cn"
        subject = "TestResult"
        plainText = ""
        
#配置连接mySql信息
class MySqlInfo():
     host='127.0.0.1'
     user='root'
     passwd='root'
     db='test'

#定义访问次数后，写入数据库
class Access_insert():
    n = 5

#定义访问频率
class Frent_query():
    n = 60
    
#定义错误日志写入文件和结果记录文件
class Record_file():
    #定义错误日志写入文件
    error_file = "d:\\Error_msg.txt"
    #定义结果记录文件
    csv_file = "d:\\csv_file.csv"
    #定义错误日志文件汇总文件
    error_total_file = "d:\\Error_msg_backup.txt"

#定义加密因子
class Sign:
    secret = "c24619ed7fef02a0ae16328146bca5f97cc6493957a2137b"


#异常日志分隔符
class Division:
    division = "glsx001"

#定义GRC调用接口地址
class GRC_Address:
    address = "http://192.168.1.37:8141/collect"
    