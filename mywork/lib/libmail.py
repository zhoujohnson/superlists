#!/bin/env python
#coding=utf-8

# -*- coding: utf-8 -*-

import email
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEAudio import MIMEAudio
import smtplib
import os.path
 
def sendEmail(authInfo, fromAdd, toAdd, ccAdd, subject, plainText, htmlPath, attachment):
        strFrom = fromAdd
        strTo = toAdd.split(',')
        strCC = ccAdd.split(',')

        server = authInfo.get('server')
        user = authInfo.get('user')
        passwd = authInfo.get('password')

        if not (server and user and passwd) :
            print 'incomplete login info, exit now'
            return

        # 设定root信息
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = strFrom
        msgRoot['To'] = toAdd
        msgRoot['CC'] = ccAdd
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        #设定纯文本信息
#        msgText = MIMEText(plainText, 'plain', 'utf-8')
#        msgAlternative.attach(msgText)
       

        #设定HTML信息
        fp = open(htmlPath, 'r')
        htmlText = fp.read()
        msgText = MIMEText(htmlText, 'html', 'utf-8')
        msgAlternative.attach(msgText)
        

       #设定内置图片信息
#        fp = open('test.jpg', 'rb')
#        msgImage = MIMEImage(fp.read())
#        fp.close()
#        msgImage.add_header('Content-Disposition', 'attachment', filename='test.jpg')
#        msgRoot.attach(msgImage)
       
       #设定附件信息
        if attachment != "":
            att1 = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            #这里的filename可以任意写，写什么名字，邮件中显示什么名字
            filename = os.path.basename(attachment)
            att1.add_header('Content-Disposition', 'attachment', filename=filename)
            msgRoot.attach(att1) 
       
       #发送邮件
        smtp = smtplib.SMTP()
        print 'Sending mail...' 
       #设定调试级别，依情况而定
#        smtp.set_debuglevel(1)
        smtp.connect(server)
        smtp.login(user, passwd)
        smtp.sendmail(strFrom, strTo+strCC, msgRoot.as_string())
        print "Sending mail done"
        smtp.quit()
        return

if __name__ == '__main__' :
        authInfo = {}
        authInfo['server'] = 'smtp.163.com'
        authInfo['user'] = 'marsyqw_2011@163.com'
        authInfo['password'] = 'yqw19861019'
        fromAdd = 'marsyqw_2011@163.com'
        toAdd = "yangqw@didihu.com.cn"
        ccAdd = "yangqw@didihu.com.cn"
        subject = 'title'
        plainText = '这里是普通文本\n'
        htmlText = '<B>HTML文本</B>'
        sendEmail(authInfo, fromAdd, toAdd, ccAdd, subject, plainText, "C:\\unintall.log","C:\\unintall.log")
