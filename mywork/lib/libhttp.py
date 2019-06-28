#!/bin/env python
#coding=utf-8

import httplib
import urllib
import sys
from conf import config
import time
  
      
def httpClient(host=config.HttpInfo.host, port=config.HttpInfo.port):
    '''  
                  此方法是建立http请求链接
         host:请求的服务器host，不能带http://开头
         port:此处没有填写 一再在host中一起将port加上 eg：'www.cwi.nl:80'
    '''
    try:
        conn = httplib.HTTPConnection(host,port, timeout=500)
        return conn
    except Exception, e:
        print e
        print sys.exc_info()


#def httpGetRequest(conn, url):
#    '''
#              此方法是发送GET请求
#       conn:是指HTTPConnection对象，即上面返回的conn
#       url: 请求的路径  eg：'/index.html'
#    '''
#   
#    for times in range(3):
#        err = None
##        print "22"
#        try:
#            conn.request("GET", url)
#        except Exception, e:
#            err = e
#            print err
#        if err == None:
#            response = conn.getresponse()
#            return response
#            break
#        print "11"
#        time.sleep(2)
      
def httpGetRequest(conn, url):
    '''
              此方法是发送GET请求
       conn:是指HTTPConnection对象，即上面返回的conn
       url: 请求的路径  eg：'/index.html'
    '''
    conn.request("GET", url)
    response = conn.getresponse()
    return response

if __name__ == '__main__':
    #测试方法
    url="/csp/city/getCityList?appKey=020e069b809a42e398454201c62cda95&v=1.0&format=xml&pageSize=10&curPage=1"
    conn = httpClient()
    print config.HttpInfo.host+url
    res = httpGetRequest(conn, url)
    print res.read()

       
       