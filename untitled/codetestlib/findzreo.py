"""
设计一个算法，计算出n阶乘中尾部零的个数
样例
11! = 39916800，因此应该返回 2
思路：先求阶乘，然后用循环获取尾部是0的个数
算法！ 算法！
"""
def findZero(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    print(sum)
    s_sum = str(sum)
    count = 0
    for i in range(1,len(s_sum)):
        if s_sum[-i] == '0':
            count = count + 1
        if s_sum[-i] != s_sum[-i-1]:
            break
    return count
print(findZero(2009))

"""
分析：
一般类似的题目都会蕴含某种规律或简便方法的阶乘末尾一个零表示一个进位，则相当于乘以10而10 是由2*5所得，
在1~100当中，可以产生10的有：0 2 4 5 6 8 结尾的数字，显然2是确定的，因为4、6、8当中都含有因子2，
所以都可看当是2，那么关键在于5的数量了那么该问题的实质是要求出1~100含有多少个5由特殊推广到一般的论证过程可得：
1、 每隔5个，会产生一个0，比如 5， 10 ，15，20.。。
2 、每隔 5×5 个会多产生出一个0，比如 25，50，75，100
3 、每隔 5×5×5 会多出一个0，比如125
"""
def sfindZero(n):
    re = 0
    while n:
        re += n//5
        n = n//5
    return re
print(sfindZero(2009))