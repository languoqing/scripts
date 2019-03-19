import urllib.request
import http.cookiejar

def url_post(url,data,header):
    req = urllib.request.Request(url,data=data,headers=header) # request 对象
    result = urllib.request.urlopen(req).read()
    return result

def url_get(url,header):
    req = urllib.request.Request(url,headers=header)
    result = urllib.request.urlopen(req).read()
    return result

if __name__ == '__main__':
    user = 'languoqing1',
    pwd = 'languoqing1'
    #设置cookie
    cj = http.cookiejar.CookieJar() #cookie 对象
    cookieHandle = urllib.request.HTTPCookieProcessor(cj) #操作cookiehandle
    openerObj = urllib.request.build_opener(cookieHandle) #创建opener对象
    urllib.request.install_opener(openerObj) #调用urlopen()使用安装的opener
    post_data = {
        'accountType': 'paw',
        'loginName': user,
        'pwd': pwd,
        'client_id': 'IN_000005',
        'redirect_uri': 'http://9test31-wap.stg3.1768.com/?act=login&st=login_callback',
        'response_type': 'code',
        'platform': 'WEB',
        'media_source': 'game_wap',
        'display': 'mobile',
        'otherLogin': 'QQ|WEIBO|WEIXIN|YIQIANBAO|HAOYISHENG',
        'state': 'eyJzdGF0ZSI6Ijg2MDEzZmMyOTkyMjMzMDVlMTNmMjUzY2Y2NTE1NzFiIiwiZnJvbSI6IiIsImFwcGtleSI6IiIsInNlcnZlcklkIjoiIiwibG9naW5Tb3VyY2UiOiIifQ==',
        'isapp': '1',
        'back_js': '',
        'back_url': 'http://9test31-wap.stg3.1768.com/?act=game_ninelamp',
        'back_flag': '1',
        'register_step2': '',
        'tabs': 'paw|wlt|toa'
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

    url_post('https://passport2-stg3.1768.com/pass-info/oauth2/loginPassport.shtml',post_data,header)

    bet_data = {
        'amount':200,
        'isAuto':0,
        'TCoin':0,
        'TScore':0,
        'caijin':0,
        'caifen':0,
        'jiankangjin':0,
        'tingdou':0,
        'wltScore':0
    }
    url_post('http://9test31-wap.stg3.1768.com/?act=game_ninelamp&st=play',bet_data,header)









