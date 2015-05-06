# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:48:11 2015
关于日期年份计算的函数库
@author: robin
"""

####################################
##函数：is_leap_year(year)
##用途：判断给定的year数字年份是否是闰年
def is_leap_year(year):
    if ((year%4)==0) and ((year%100)>0):
        return True
    elif (year%400)==0:
        return True
    else:
        return False

