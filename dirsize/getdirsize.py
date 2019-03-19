#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
author: languoqing
date:2017-03-31
获取路径下文件夹的大小
'''
import os

def getdirsize(dirpath):
    list_dir = os.listdir(dirpath)
    for i in list_dir:
        if os.path.isdir(os.path.join(dirpath,i)):
            os.chdir(os.path.join(dirpath,i))
            print('%s size %s ' % (i,os.popen('du -sh').read()))

if __name__ == '__main__':
    dirpath = input('请输入路径：')
    getdirsize(dirpath)