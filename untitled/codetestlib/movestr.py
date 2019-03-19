"""
给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
对于字符串 "abcdefg".
offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
"""
def movestr(offset,str):
    len_str = len(str)
    for i in range(offset+1):
        if offset == 0: return str
        temp_str = str[-i:] + str[:-i]
        print(temp_str)
movestr(3,'abcdefg')

