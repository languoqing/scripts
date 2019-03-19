
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

#webdriver 添加到执行
webdriver_chrom = "D:\selenium\chromedriver.exe"
os.environ['webdriver-chrom'] = webdriver_chrom
#去掉浏览器顶部窗口报错
optinos = webdriver.ChromeOptions()
optinos.add_experimental_option('excludeSwitches',['ignore-certificate-errors'])
obj_chrom = webdriver.Chrome(webdriver_chrom,options=optinos)
obj_chrom.set_window_size(380,750)
url = 'http://9test64-wap.stg3.1768.com/?act=game_shaizile'
try:
    obj_chrom.get(url)
except Exception as e:
    print('请求错误 ++++ %s'.format(e))
def is_xpth(xpth):
    w = wait.WebDriverWait(obj_chrom,30)
    elem = w.until(lambda a : a.find_element_by_xpath(xpth))
    if elem:
        return True
    return False

action = ActionChains(obj_chrom)


if is_xpth('/html/body/div[3]/div[7]/div/div[2]/span[2]'):
    #action.move_to_element(obj_chrom.find_element_by_xpath('//*[@id="KADANG"]/div[4]/div/div[2]/span[4]')).click_and_hold(obj_chrom.find_element_by_xpath('//*[@id="KADANG"]/div[4]/div/div[2]/span[4]')).perform()
    time.sleep(5)
    obj_chrom.find_element_by_xpath('/html/body/div[3]/div[7]/div/div[2]/span[2]').click()
time.sleep(6)
if 'passport' in obj_chrom.current_url:
    time.sleep(3)
    obj_chrom.find_element_by_id('pawUname').send_keys('languoqing6')
    obj_chrom.find_element_by_id('pawUpwd').send_keys('languoqing6')
    obj_chrom.find_element_by_id('pawCommitBtn').click()
    time.sleep(3)
#记日志：登录成功
if 'showFootBar' in obj_chrom.current_url:
    obj_chrom.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/a').click()
time.sleep(5)
btn = obj_chrom.find_elements_by_xpath('//*[@id="scoreHover"]/div')


#开始回归用例
#按钮押注
obj_chrom.find_element_by_xpath('//*[@id="ipt_yazhu"]').click()
obj_chrom.find_element_by_xpath('//*[@id="scoreHover"]/div/div[2]').click()
time.sleep(3)
obj_chrom.find_element_by_xpath('//*[@id="start"]').click()
time.sleep(3)
obj_chrom.save_screenshot('D:\\Users\\ex-languoqing600\\PycharmProjects\\untitled\\pythonselenium\\image\\a.png')

#输入押注
# obj_chrom.find_element_by_xpath('//*[@id="ipt_yazhu"]').clear()
# time.sleep(3)
# obj_chrom.find_element_by_id('ipt_yazhu').send_keys(100)
# time.sleep(5)
# obj_chrom.find_element_by_xpath('//*[@id="start"]').click()
# time.sleep(3)

#排行榜
# atime.sleep(5)
# obj_chrom.find_element_by_xpath('//*[@id="inpage"]').click()
# time.sleep(2)
# obj_chrom.save_screenshot('D:\\Users\\ex-languoqing600\\PycharmProjects\\untitled\\pythonselenium\\image\\{}.png'.format('pahangbang'))
# obj_chrom.find_element_by_xpath('//*[@id="tabs"]/ul[1]/li[1]//*[@id="tabs"]/ul[1]/li[1]').click()
# time.sleep(2)
# obj_chrom.save_screenshot('D:\\Users\\ex-languoqing600\\PycharmProjects\\untitled\\pythonselenium\\image\\{}.png'.format('pahangbang'))
#

