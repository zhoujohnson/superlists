# -*- coding: utf-8 -*-
import os,sys

class DBLibrary:
    def __init__(self):
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        # conn = ''
        # host = ''
        # db = ''
        # user = ''
        # psw = ''
        reload(sys)        
        sys.setdefaultencoding('utf-8')
    def create_conn_param(self, host, db, user, psw):
        self.host = host
        self.db = db
        self.user = user
        self.psw = psw

        
    def conn_data(self, dbModuleName):
        """

        :param dbModuleName:
        """
        # global pyodbc
        if dbModuleName == "Oracle":
            try:
                import cx_Oracle           
            except ImportError, e:
                print e
            dsn = cx_Oracle.makedsn(self.host, self.db, 1521)
            print dsn
            self.conn = cx_Oracle.connect(self.user, self.psw, dsn)
            
        elif dbModuleName == "Mysql" or "MSSql":
            try:
                import pyodbc
            except ImportError, e:
                print e
            dsn = 'SERVER=' + self.host + ';DATABASE=' + self.db + ';UID=' + self.user + ';PWD=' + self.psw 

            if dbModuleName == "Mysql":   
                driver = 'DRIVER={MySQL ODBC 5.1 Driver};' + dsn

                self.conn = pyodbc.connect(driver)
            else:
                driver = 'DRIVER={SQL Server};' + dsn
                self.conn = pyodbc.connect(driver)       
            
    def query_data(self, sql):
        cur = self.conn.cursor() 
        cur.execute(sql)
        row = cur.fetchall()
        cur.close()
        return row

    def insert_data(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()


    def update_data(self, sql):
        self.insert_data(sql)

    def delete_data(self, sql):
        self.insert_data(sql)

    def close_database(self):
        self.conn.close()


if __name__ == '__main__':
    db = DBLibrary() 
    db.create_conn_param("192.168.1.229","glsx_ds","test","123456")
    db.conn_data("Mysql")

    sql="SELECT * from ds_marketing_record"
    
    row = db.query_data(sql)
    print row
#TYPE_type = {"SEX":"sex", "HOBBY":"hobby"}
#
#idlist = []
#
#sql="select id from info GROUP BY  id "
#row = db.query_data(sql)
#
#for idTuple in row:
#    id = idTuple[0]
#    sql="select type from info WHERE id=%d" %id
#    row = db.query_data(sql)
#    typelist=[]
#    for typeTuple in row:
#        if typeTuple[0] not in typelist:
#            typelist.append(typeTuple[0])
#
#    sqlList=""
#
#    for TYPE in typelist:
#        #将各个类型对应的值都取出来保存在列表中
#        sql = "select value from info where type='%s' and id=%d" % (TYPE,id)
#        row = db.query_data(sql)
#        valueList = []
#        typeList = []
#        for valueTuple in row:
#            valueList.append(valueTuple[0])
#        #将值连接起来    
#        linkValue=""
#        for value in valueList:
#            value="\'" + value + "\'"
#            linkValue+=value + ','
#        linkValue = "(" + linkValue.strip(",") + ")"
#
#        sqlList +='and ' + "%s in %s " %(TYPE_type[TYPE],linkValue)
#        sqlList = sqlList.strip("and")
#        
#    sqlResult = "select * from user where"
#    sqlResult = sqlResult + sqlList
#    print sqlResult
#    row = db.query_data(sqlResult)
#    for i in row:
#        print i