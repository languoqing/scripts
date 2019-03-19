import os
list_dir = os.listdir('/data/httpd/')
for x in list_dir:
    c_path = os.path.join(list_dir,x)
    os.chdir(c_path)
    print(os.curdir)
    #os.popen('rm -rf *')
