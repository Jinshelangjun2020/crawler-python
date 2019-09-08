#coding=utf-8
import requests
from bs4 import BeautifulSoup

pageUrl = "https://www.meitulu.com/t/tuigirl/"
tutu9 = "http://www.tutu9.com"

response = requests.get(tutu9)

pageContent = response.content

pageSoup = BeautifulSoup(pageContent, 'html.parser')

#找到导航页美女列表
tutu_index_nav = pageSoup.find("div", class_='nav')
tutu_index_nav_ul = tutu_index_nav.find("ul")
tutu_index_nav_ul_li = tutu_index_nav_ul.find_all('li')
for li in tutu_index_nav_ul_li:
    li_a = li.find('a')
    if li_a:
        url = li_a.get('href')
        print ("nav url is %s" % (url))




