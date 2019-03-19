#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
author: languoqing
date:2017-04-01
找到建立的空目录
'''
import os
def findemptydir(path):
    list_dir = os.listdir(path)
    list_file = []
    for d in list_dir:
        print('++++++++ %s +++++++' % d)
        f = os.path.join(path,d)
        if os.path.isdir(f):
            child_dir = os.listdir(f)
            for cd in child_dir:
                filepath1 = os.path.join(f,cd)
                if os.path.isdir(filepath1):
                    if not os.listdir(filepath1):
                        print('%s ====== %s' % (d,cd))
                        list_file.append(d)
                else:
                    data = open(filepath1).read()
                    if len(data) == 0:
                        print('%s ====== %s' % (d,cd))
                        list_file.append(d)
    return list_file



if __name__ == '__main__':
    filepath = input('请输入路径：')
    with open('t.txt','w+') as f:
        f.write(findemptydir(filepath))
        f.close()
    findemptydir(filepath)
