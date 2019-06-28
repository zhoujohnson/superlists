# -*- coding: utf-8 -*-
import MySQLdb
import shutil
import sys

def connMySql(host='127.0.0.1', user='root', passwd='123456', 
              db="test", port=3306, charset='utf8'): 
    ''' 
              此方法用来和数据库建立连接，并返回连接对象
             
             参数：
       host:连接的数据库服务器主机名   
       user:连接数据库的用户名
       passwd:连接密码
       db:连接的数据库名
       port:指定数据库服务器的连接端口，默认是3306
       charset:编码方式
    '''
    try:
        conn = MySQLdb.connect(host, user, passwd, db, port=port, charset=charset)
        return conn
    except Exception,ex:
        print ex
   

def sqlSelect(sql,conn):
    
    """
                此方法用于数据库查询操作，以列表的形式返回执行结果
              
               参数：
        sql:查询的sql语句
        conn：数据库连接对象
    """
    cur=conn.cursor()
    cur.execute(sql)
    rs=cur.fetchall()
    cur.close()
    return rs


def sqlSelectin(sql,conn):
    
    """
                此方法用于数据库查询操作，以列表的形式返回执行结果
              
               参数：
        sql:查询的sql语句
        conn：数据库连接对象
    """
    cur=conn.cursor()
    cur.executemany(sql)
    rs=cur.fetchall()
    cur.close()
    return rs

def sqlDML(sql,conn):
    #include: insert,update,delete
    cr=conn.cursor()
    cr.execute(sql)
    cr.close()
    conn.commit()
    
def insert_data(sql,conn):
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()

def insert_manyData(sql,list_data,conn):
    cur = conn.cursor()
    cur.executemany(sql,list_data)
    conn.commit()
    cur.close()

def update_data(sql, conn):
    insert_data(sql, conn)


if __name__ == "__main__":
    conn = connMySql(host="192.168.1.229", user="test", passwd="123456", db="test", port=3306, charset='utf8')

    testname = "http"
    result = "pass"
    sql = "insert into testrecord(test_name,result) values(\"%s\", \"%s\")" % (testname,result)
    print sql
    insert_data(sql, conn)
    #print "ok"
    