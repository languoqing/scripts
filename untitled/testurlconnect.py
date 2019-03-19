import configparser
import os
import re

"""获取游戏对应端口"""
def getPort(filename):
    game_name = filename.split('.')[0]
    try:
        port = conf.get("game-port",game_name)
        return port
    except Exception as e:
        print(game_name+ "没有端口，请检查")

"""备份文件"""
def movefile(surcedir,tardir,surcefile):
    with open (os.path.join(surcedir,surcefile),'r+') as f:
        for x in f.readlines():
            with open(os.path.join(tardir,surcefile),'a+') as d:
                d.write(x)
    os.remove(os.path.join(surcedir,surcefile))



"""匹配到httpURL"""
def findUrl(url):
    p = re.compile(r"(http[^']+)")
    match = p.search(url)
    if match:
        return match.group()

"""替换链接URL"""
def replaceFile(bakfile,newfile,bakdir,confidir,port):
    print(bakfile)
    print(newfile)
    with open('%s%s'% (bakdir,bakfile),'r+') as f:
        for x in f.readlines():
            url = findUrl(x)
            if not url:
                print(url)
                print(x)
                with open('%s%s'% (confidir,newfile),'a+') as d:
                    d.write(x)
            else:
                with open('%s%s' % (confidir,newfile),'a+') as d:
                    d.write(x.replace(url,'https://node-test.games.1768.com:%s/' % port))


"""删除备份文件"""
def remBakFile():
    os.popen('rm -rf *')

if __name__ == '__main__':
    gamehj = input("输入你要更新的环境（eg:game31）：")
    game_path = "/data/httpd/%s/wap/app/config/" % gamehj
    configbakdir = os.path.join(game_path, 'configbak/')
    if os.path.exists(configbakdir):
        os.chdir(configbakdir)
        remBakFile()
    else:
        os.mkdir(configbakdir)
    conf = configparser.ConfigParser()
    conf.read("%sgame_port.conf" % game_path)
    s_list = conf.items('game-port')
    for s in s_list:
        gamefilename = s[0]+'.php'
        movefile(game_path, configbakdir, gamefilename)
        port = getPort(s[0])
        replaceFile(gamefilename,gamefilename,configbakdir,game_path,port)



