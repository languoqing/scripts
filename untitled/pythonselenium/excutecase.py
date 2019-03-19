from untitled.pythonselenium.beforgame import getChromObj
from selenium.webdriver.support import wait
from selenium.webdriver.common.action_chains import ActionChains
import time
obj = getChromObj()
def loginGame(url,game):
    try:
        obj.get('%s/?act=%s'.format(url,game))
    except Exception as e:
        print('请求错误++++++++++%s'.format(e))
        obj.find_element_by_xpath('//*[@id="KADANG"]/div[4]/div/div[3]/span[1]').click()
    if 'passport' in obj.current_url:
        time.sleep(3)
        obj.find_element_by_id('pawdUname').send_keys(login_username)
        obj.find_element_by_id('pawUpwd').send_keys(login_pwd)
        obj.find_element_by_id('pawCommitBtn').click()
        #记日志：登录成功
    if 'showFootBar' in obj.current_url:
        obj.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/a').click()

def is_xpth(xpth):
    w = wait.WebDriverWait(obj_chrom, 30)
    elem = w.until(lambda a: a.find_element_by_xpath(xpth))
    if elem:
        return True
    return False

#操作
def btnyazhu(*ags):
    '''ags:按钮元素列表'''
    for i in ags:
        obj_chrom.find_element_by_xpath('//*[@id="ipt_yazhu"]').click()
        obj.find_element_by_xpath(i).click()
        time.sleep(3)
        obj_chrom.find_element_by_xpath('//*[@id="start"]').click()
        time.sleep(3)
        resultscreenshoot(i)

def inputyazhu(value):
    '''输入押注'''
    obj.find_element_by_xpath('//*[@id="ipt_yazhu"]').clear()
    obj.find_element_by_id('ipt_yazhu').send_keys(value)
    time.sleep(2)
    obj.find_element_by_xpath('//*[@id="start"]').click()
    time.sleep(3)
    resultscreenshoot(value)

def paihangbang(elem):
    '''排行榜'''
    obj.find_element_by_xpath(elem).click()
    time.sleep(2)
    resultscreenshoot(elem)
    obj.find_element_by_xpath('//*[@id="tabs"]/ul[1]/li[1]//*[@id="tabs"]/ul[1]/li[1]').click()
    time.sleep(2)
    resultscreenshoot('我的战绩')


def resultscreenshoot(imgname):
    '''浏览器截图'''
    obj.save_screenshot('D:\\Users\\ex-languoqing600\\PycharmProjects\\untitled\\pythonselenium\\image\\{}'.format(imgname))

