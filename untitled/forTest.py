"""list_i = []
for i in range(100):
    list_i.append(i)
print(list_i[1:-1:2])
"""
import os
game_path = "/data/httpd/31/wap/app/config/"
configbakdir = os.path.join(game_path, 'configbak/')
print(configbakdir)