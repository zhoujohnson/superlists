#!/bin/env python
#coding=utf-8

import xml.etree.ElementTree as et
import sys

#读取指定路径下的xml文件
def load_xml_file(fileName, nodeStr):
    """
              此方法是将指定路径下的xml文件加载进来，按照nodeStr指定的节点进行解析，并返回节点的值
              
       filename：xml文件
       nodeStr：指定的节点  eg：info/list[0]/hobby ===>(info指的是根节点，list是指info节点下的子节点，
       [0]是指第一个list节点以此类推， hobby是最终要解析的节点) 
    """
    try:
        root = et.parse(fileName).getroot()  #获取跟节点
        allNodeList = nodeStr.split('/')
        del allNodeList[0]
        for i in allNodeList:
            root = findNode(root, i)
        return root.text.encode('utf-8')
    except Exception, e:
       print e
       print sys.exc_info()
       

def load_xml(xmlVar, nodeStr):
    """
             此方法是指将指定的xml字符串，根据提供的节点值进行解析，最终返回解析的节点的那个值
       
      xmlVar：xml字符串
      nodeStr:指定的节点  eg：info/list[0]/hobby ===>(info指的是根节点，list是指info节点下的子节点，
       [0]是指第一个list节点以此类推， hobby是最终要解析的节点) 
    """
    try:
        root = et.fromstring(xmlVar)
        allNodeList = nodeStr.split('/')
        del allNodeList[0]
        for i in allNodeList:
           root = findNode(root, i)
        #print root
        result = root.text.encode('utf-8')
        return result
    except Exception, e:
        noValue=''
        return noValue



#查找节点      
def findNode(root,node):
    nodeElement=''
    if '[' in  node:
        nodeList = node.split('[')
        allnode = root.findall(nodeList[0])
        nodeIndex = nodeList[1].strip(']')
        nodeElement = allnode[int(nodeIndex)]
        
    else:
        nodeElement = root.find(node)
    return nodeElement
    
if __name__ == '__main__':
#    load_xml_file('../testcase/doc1.xml', 'info/list[0]/hobby')
    xmlstr='''
          <root>
          <person1>
          <name>侯春朋</name>
          <sex>男</sex>
          <age>26</age>
          </person1>
          <person1>
          <name>侯春朋1</name>
          <sex>男</sex>
          <age>26</age>
          </person1>
          </root> 
          '''
    nodeStr="root/person1[1]/name"       
#    test = _xmlKeywords()
#load_xml(xmlstr, nodeStr)