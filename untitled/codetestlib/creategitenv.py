import os
import sys
import logging
import shutil
import subprocess
logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)
loger.setLevel(logging.INFO)
current_path = ''
branch_name = ''
def excuteCmd(cmd):
    try:
        p = subprocess.Popen(args=cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        p.wait()
        loger.info('{}  执行成功'.format(cmd))
    except Exception as e:
        loger.info('=={}== 执行错误，错误为：{}'.format(cmd,e))

try :
    current_path = input('输入你的环境名,eg:game4 ：').strip()
    branch_name = input('你要拉取的分支名,eg:master：').strip()
except Exception as e:
    print('输入有错误 ===={}====='.format(e))

loger.info('开始删除当前wap环境')
try:
    shutil.rmtree('/data/httpd/{}/wap'.format(current_path))
    loger.info('删除成功')
except Exception as e:
    loger.info('wap文件夹删除失败')
os.mkdir('/data/httpd/{}/wap'.format(current_path))
os.chdir('/data/httpd/{}/wap'.format(current_path))
loger.info('开始创建分支')
excuteCmd('git init')
excuteCmd('git remote add origin http://www:12345678@21.56.65.1/wlt_game_php/gamehall.git')
excuteCmd('git fetch --depth=1')
excuteCmd('git checkout -b {} origin/{}'.format(branch_name,branch_name))
loger.info('创建完成')
loger.info('cpye config配置文件')
os.popen('cp -r /data/httpd/game66_config /data/httpd/{}/wap/app/config.php'.format(current_path))
loger.info('已经完成了')


# shutil.copyfile('/data/httpd/game66_config','/data/httpd/{}/wap/app/config.php')
