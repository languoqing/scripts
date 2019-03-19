import  os
def movefile(surcedir,tardir,surcefile):
    with open (os.path.join(surcedir,surcefile),'r+') as f:
        for x in f.readlines():
            with open(os.path.join(tardir,surcefile),'a+') as d:
                d.write(x)

if __name__ == '__main__':
    gamelist = os.listdir('/data/httpd/')
    for game in gamelist:
        movefile('/data/httpd/%s/wap/app/config.php'% game,'/data/httpd/config_bak/%s_wap_config.php'%game)
        movefile('/data/httpd/%s/pc/app/config.php' % game, '/data/httpd/config_bak/%s_pc_config.php' % game)
