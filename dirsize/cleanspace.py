#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
author: languoqing
date:2017-03-31
删除不需要分支清理空间
'''
import os

def cleanbranch(dirpath):
    os.chdir(dirpath)
    branchs = os.popen('git branch')
    os.popen('git checkout master')
    for b in branchs.readlines():
        if 'master' != b:
            os.popen('git branch -D %s'% b)
    print('清除成功！')

if __name__ == '__main__':
    dirpath = input('请输入路径：')
    cleanbranch(dirpath)
