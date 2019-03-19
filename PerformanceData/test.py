#-*- coding:utf-8 -*-
import subprocess



if __name__ == '__main__':
    a = subprocess.check_output("adb shell ps | findstr {}".format("com.pingan.gamehall"),shell=True,encoding='GB2312')
    print(a.split("\n")[0].split(" ")[3])
    
    
    
    

    