'''需求：爬取网易云的评论超过999+的歌曲，按照评论数量排序
1、获取网易云页面资源
2、找到评论字段
3、累计评论，获取歌曲名
问题：怎么一首首歌去爬取？（选取主题）
'''
from bs4 import BeautifulSoup
import requests
song_id = dict(id = 186016)
r = requests.post('http://music.163.com/#/song',data=song_id)
soup = BeautifulSoup(markup,"lxml",r.text)
# print(soup.prettify())
print(soup.b)
#print(soup.find_all('link'))

