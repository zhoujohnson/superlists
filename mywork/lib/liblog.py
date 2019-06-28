# -*- coding: utf-8 -*-
import logging

def initLog(logfile):
    #创建一个logger
    logger = logging.getLogger()
    #设置logger的级别  
    logger.setLevel(logging.DEBUG)   
    #创建console handler
    ch = logging.StreamHandler()
    #设置级别
    ch.setLevel(logging.DEBUG)
    #设置logger的输出格式
    formatter = logging.Formatter("%(asctime)s[%(levelname)-8s][module:%(module)s,line:%(lineno)04d]%(message)s")
    #设置ch的格式
    ch.setFormatter(formatter)
    #把ch添加到logger中 
    logger.addHandler(ch)
    
    fh = logging.FileHandler(logfile)  
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)    
    logger.addHandler(fh)  
    return logger


if __name__ == '__main__':
    logger = initLog("test.log")
    logger.debug("debug message")  
    logger.info("info message")  
    logger.warn("warn message")  
    logger.error("error message")  
    logger.critical("critical message") 
