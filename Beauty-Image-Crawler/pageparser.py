#coding=utf-8
from bs4 import BeautifulSoup
from downloader import DownLoader

class PageParser:
    hasDownloadedUrl = set()
    def __init__(self):
        print(self)
        print(self.__class__)


    @staticmethod
    def extractImageUrl(url):
        if url in PageParser.hasDownloadedUrl:
            print ("we has downloaded url %s" %(url))
            return

        pageContent = DownLoader.downLoadPage(url)
        pageSoup = BeautifulSoup(pageContent, 'html.parser')
        fuck = pageSoup.find_all(class_='content_img')
        for image in fuck:
            imageUrl = image.get("src")
            '''DownLoader.getBigImage("https://www.meitulu.com/img.html?img="+imageUrl)'''
            DownLoader.downloadImage(imageUrl)

        PageParser.hasDownloadedUrl.add(url)

        #抽取列表页美女图#
        currentGirlSubPages = pageSoup.find(attrs={'id': 'pages'})
        girlPages = currentGirlSubPages.find_all('a')
        prefixUrl = "https://www.meitulu.com"
        for page in girlPages:
            subImgUrl = page.get('href')
            print("sub tuigirl image url %s" %(subImgUrl))
            PageParser.extractImageUrl(prefixUrl + subImgUrl)





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


        #是否找到foot分页
        pages = soup.find(attrs={'id': 'pages'})
        imgPageA = pages.find_all('a')
        for img_page in imgPageA:
            img_page_a_href = img_page.get('href')
            if 'html' in img_page_a_href:
                sub_page = DownLoader.downLoadPage(img_page_a_href)
                PageParser.parserForImageUrl(sub_page)


        #tag_ul 下载图集分类
        otherBeautyUl = soup.find(attrs={'id': 'tag_ul'})
        lis = otherBeautyUl.find_all('li')
        for li in lis:
            a = li.find('a')
            tag_page_url = a.get('href')
            tag_name = a.get('text')
            print("tag page url %s" %(tag_name))

            tag_page_content = DownLoader.downLoadPage(tag_page_url)

            PageParser.parserForImageUrl(tag_page_content)







