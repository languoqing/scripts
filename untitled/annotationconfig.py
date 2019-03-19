import os
"""注释config中不需要代码"""

def annotionFile(file,bakfile,*body):
    try:
        with open(file,'r+') as f:
            for r in f.readlines():
                if r.strip() not in body:
                    with open(bakfile,'a+') as d:
                        d.write(r)
                else:
                    with open(bakfile,'a+') as d:
                        d.write('##'+r)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    list_dir = os.listdir('/data/httpd/')
    list_pathdir = ['wap','pc']
    for x in list_dir:
        for y in list_pathdir:
            file_path = '/data/httpd/%s/%s/app/config.php' % (x,y)
            filebak_path = '/data/httpd/%s/%s/app/config.php.bak' % (x,y)
            annotionthing = ['','']