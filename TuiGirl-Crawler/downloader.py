#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

class DownLoader:
    imageDir = "E:\\worktest\\tuigirl"
    imageCount = 0
    def __init__(self):
        print (self)

    '''下载网页'''

    @staticmethod
    def downLoadPage(pageUrl):
        print ("try to download page %s" %(pageUrl))
        response = requests.get(pageUrl)
        if response.status_code == 200:
            print ("download page %s success" %(pageUrl))
            page_content = response.content
            return page_content

    '''下载图片'''

    @staticmethod
    def downloadImage(imgUrl):
        print ("try to download image %s" %(imgUrl))
        response = requests.get(imgUrl)
        img = response.content
        print (img)
        if response.status_code == 200:
            try:
                path = "E:\\worktest\\tuigirl\\%d.jpg" % DownLoader.imageCount
                DownLoader.imageCount += 1
                with open(path, 'wb') as f:
                    f.write(img)
            except Exception as ex:
                print ("...error but we go on...")
                pass
        else:
            print ("can not get image %s" %(imgUrl))



    @staticmethod
    def getBigImage(url):
        bigImgPageContent = DownLoader.downLoadPage(url)
        bigImgPageSoup = BeautifulSoup(bigImgPageContent, 'html.parser')
        imgList = bigImgPageSoup.find_all('img')
        for image in imgList:
            src = image.get('src')
            if 'images' in src:
                print ("haha src %s" % (src))





