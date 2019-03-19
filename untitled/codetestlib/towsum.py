import sys
import logging
logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)
loger.setLevel(logging.INFO)
sys.setrecursionlimit(1000000)
"""
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1
"""
# def getIndexFormList(args,tarsum):
#     for i in range(len(args)):
#         for y in range(len(args[i:])):
#             if i == y:
#                 continue
#             if tarsum == args[i] + args[y]:
#                 print('第一个数i{},下标为：{}，第二个数y{}，下标为：{}'.format(args[i],i,args[y],y))
#                 return i,y
#     print('没有找到')
#
# list_1 = [1,2,4,6,3,8]
# num = 7
# getIndexFormList(list_1,num)

"""
二分查找法,找出值后返回索引，target，给出一个数a ,b = target - a，寻找b
"""
#二分查找
def binrySearch(l,min,max,num):
    loger.info('传进来的参数是{}，{}，{}，{}'.format(l,min,max,num))
    if min > max:
        loger.info('没有找到')
        return False
    midl = (min + max)//2
    if l[midl] == num:
        loger.info('找到了，是{}'.format(l[midl]))
        return True
    elif num < l[midl]:
        return binrySearch(l,min,midl-1,num)
    else:
        return binrySearch(l,midl+1,max,num)

#找出和为sum 的两个数
def getIndexFormList(args,sum):
    sort_list = sorted(args)
    loger.info('排序后的列表{}：'.format(sort_list))
    for i in args:
        loger.info('{}开始'.format(i))
        y = sum - i
        loger.info('y是：{}，i是：{}'.format(y,i))
        if binrySearch(sort_list,0,len(args)-1,y):
            return i,y
        else:
            loger.info('不存在这样的两个数')
            return i, None
    loger.info('循环结束')
    return


if __name__ == '__main__':
    lis = [2,3,4,1,7,5,18]
    a,b = getIndexFormList(lis,29)
    print(a)
    print(b)