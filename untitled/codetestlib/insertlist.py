'''
Insert (2, 5) into [(1,2), (5,9)], we get [(1,9)].
Insert (3, 4) into [(1,2), (5,9)], we get [(1,2), (3,4), (5,9)].
'''
#两种情况，重叠和不重叠
def insertList(target,source):
    result = []
    for i in source:
        #没有重叠
        if target[-1] < i[0]:
            result.append(target)
        #重叠
        elif target[0] > i[0] and target[-1] < i[-1]:
            result.append(i)
        else:
            result.append(i)
    return result
targetlist = []