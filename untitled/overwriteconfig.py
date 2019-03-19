import os
path = '/usr/local/nginx-1.4.7/conf/vhosts/https/'
list_conf = os.listdir(path)
for game in list_conf:
    with open(path.join(game),'r+') as f:
        with open(path.join('game.conf'),'a+') as f2:
            f2.write('###########%s'% game)
            for x in f.readlines():
                if x == '':
                    pass
                else:
                    f2.write(x)
            f2.write('/n')
