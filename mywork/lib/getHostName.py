#coding=utf8
def getHostName():
    #获取主机的IP地址
    import socket
    t = socket.gethostbyname(socket.gethostname())
    #print t,type(t)
    return t
