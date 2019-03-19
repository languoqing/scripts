"""
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target
字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
思路：拿到tar的字符长度，循环去source字符循环比较
"""
def findString(Sources,Tars):
    tar_len = len(Tars)
    i_len = 0
    for i in range(len(Sources)):
        if Sources[i:tar_len] == Tars:
            print(Sources[i:tar_len])
            return 1
        else:
            tar_len +=1

if __name__ == '__main__':
    a = findString('agshdgdhd','dgdh')
    print(a)



