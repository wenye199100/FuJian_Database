#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/3/7 11:23 
# @Author : yewenwen 
# @Site :  
# @File : list.py.py 
# @Software: PyCharm

from django.shortcuts import render_to_response

address = [
    {'name': '张三', 'address': '地址一'},
    {'name': '李四', 'address': '地址二'}
]

def index(request):
    return render_to_response('list.html', {'address': address})