#-*- coding:utf-8 -*-
import subprocess


def check_device_online():
    """
    检查设备连接
    :return: 0 连接，1 未连接
    """
    if subprocess.check_output("adb devices", shell=True, encoding='GB2312').strip() != "List of devices attached":
        return 0
    else: print("check device connecting")

def get_device():
    if check_device_online() == 0:
        check_device_online()
        device = subprocess.check_output("adb devices",shell=True,encoding='GB2312')
        return device.split("\n")[1].split("\t")[0].strip()
    
    

def get_PID(pakage_name):
    """
    获取进程pid
    :param pakage_name:
    :return:
    """
    if check_device_online() == 0:
        re = subprocess.check_output("adb shell ps | findstr {}".format(pakage_name),shell=True,encoding='GB2312')
        pid = re.split("\n")[0].split(" ")[3]
        return pid
        
    
    
    
    
    

def get_memory_cpu(device,pakage_name):
    """
    获取进程使用的内存情况:"adb -s device_name shell top -n 1 | grep pakage_name"
    :param pakage_name:
    :return:
    """
    if check_device_online() == 0:
        a = "adb -s {} shell top -n 1 | findstr {}".format(device,pakage_name)
        str_memory = subprocess.check_output(a,shell=True, encoding='GB2312')
        list_memory = str_memory.split(" ")
        re_memory = float(list_memory[12].replace("K"," ").strip(" ")) / 1024 ##换算MB
        re_cpu = list_memory[5]
        return (re_memory,re_cpu)


def get_flow(device,pid):
    """
    获取进程的流量情况：adb -s devices shell cat /proc/PID/net/dev
    :param device:
    :param PID:
    :return: dic
    """
    if check_device_online() == 0:
        re_list = {}
        a = subprocess.check_output("adb -s {} shell cat /proc/{}/net/dev".format(device,pid), shell=True, encoding='GB2312')
        b = a.split("\n")
        for i in b:
            if "wlan0:" in i:
                re_list['rev'] = i.split(" ")[2]
                re_list['send'] = i.split(" ")[40]
                break
        return re_list
    
def get_battery(device,pid):
    """
    获取设备当前电量adb -s "+ Main.devices+" shell dumpsys battery
    :return:
    """
    if check_device_online() == 0:
        a = subprocess.check_output("adb -s {} shell cat /proc/{}/net/dev".format(device,pid), shell=True, encoding='GB2312')
        re = a.strip().split(":")[1].strip()
        return re
    
if __name__ == '__main__':
    a , b = get_memory_cpu(get_device(),"com.pingan.gamehall")
    print(a,b)
    
    
    
    
    