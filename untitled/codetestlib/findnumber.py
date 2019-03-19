"""
计算数字k在0到n中的出现的次数，k可能是0~9的一个值
思路，自己、大于自己的n*10余0，除以n*10 余n
"""
def findNumber(k,n):
    count = 0
    for i in range(1,n+1):
        if k == i or i//10 == k or i-(i//10)*10 == k :
            count += 1
            print('i:'+str(i))
    return count
print(findNumber(3,100))

"""网上的答案错了，31,32"""
class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        assert(n >= 0 and 0 <= k <= 9)
        count = 0
        for i in range(n + 1):
            j = i
            while True:
                if j % 10 == k:
                    print(j)
                    count += 1
                j /= 10
                if j == 0:
                    break
        return count

a= Solution()
print(a.digitCounts(3,100))
