#coding=utf-8
from bs4 import BeautifulSoup
from downloader import DownLoader

class PageParser:
    def __init__(self):
        print(self)
        print(self.__class__)


    @staticmethod
    def extractImageUrl(url):
        pageContent = DownLoader.downLoadPage(url)
        pageSoup = BeautifulSoup(pageContent, 'html.parser')
        fuck = pageSoup.find_all(class_='content_img')
        for image in fuck:
            imageUrl = image.get("src")
            '''DownLoader.getBigImage("https://www.meitulu.com/img.html?img="+imageUrl)'''
            DownLoader.downloadImage(imageUrl)

    """
    Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
    """
    @staticmethod
    def parserForImageUrl(pageContent):
        if len(pageContent) == 0 :
            print ("pageContent is empty.")
            return
        soup = BeautifulSoup(pageContent, 'html.parser')

        """
        找到美女列表页的盒子区
        """
        tuigirlUl = soup.find_all("ul", "img")

        for ul in tuigirlUl:
            tuigirlImgs = ul.find_all('a')
            for url in tuigirlImgs:
                href = url.get('href')
                if 'item' in href:
                    print (href)
                    '''DownLoader.downloadImage(href)'''
                    PageParser.extractImageUrl(href)






