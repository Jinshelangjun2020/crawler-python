#coding=utf-8
from bs4 import BeautifulSoup
from duotu555_page_downloader import Duotu555PageDownloader
from image_info import ImageInfo

class Duotu555PageParser:
    classify_index_page_url_set = set()

    @staticmethod
    def parserPage(pageContent):
        pageSoup = BeautifulSoup(pageContent, 'html.parser', from_encoding="gb18030")
        # 获取主页导航列表url
        Duotu555PageParser.extract_head_nav_image_url(pageSoup)
        # 获取 https://www.duotu555.com/*/index.html 页面主题图片url
        Duotu555PageParser.get_page_box_image_url()


    # 获取主页head中nav的分类
    @staticmethod
    def extract_head_nav_image_url(pageSoup):
        if not pageSoup:
            print ("duotu index pageSoup is none")
            return

        # 首页分类ul 只获取国产，日韩，欧美三个分类
        head_nav_ul = pageSoup.find('ul', class_='menu')
        # 首页分类ul中的li
        head_nav_ul_lis = head_nav_ul.find_all('li')
        if head_nav_ul_lis:
            for li in head_nav_ul_lis:
                if li:
                    a_li = li.find('a')
                    if a_li:
                        a_text = a_li.text
                        print ("a_text %s" %(a_text))
                        if '国产' in a_text or '日韩' in a_text or '欧美' in a_text:
                            classify_page_url = a_li.get('href')
                            print ("分类：%s" %(classify_page_url))
                            Duotu555PageParser.classify_index_page_url_set.add(classify_page_url)


        # 获取精品套图中的分类url
        head_taotu = pageSoup.find('ul', class_='tag_ul')
        if head_taotu:
            taotu_lis = head_taotu.find_all('li')
            if taotu_lis:
                for li in taotu_lis:
                    a = li.find('a')
                    if a:
                        classfy_url = a.get('href')
                        classfy_text = a.text
                        print ("get %s , url = %s" %(classfy_text, classfy_url))
                        Duotu555PageParser.classify_index_page_url_set.add(classify_page_url)


    # 获取主页box中美女主页url
    # 比如获取url: https://www.duotu555.com/mm/32/35204.html
    @staticmethod
    def get_page_box_image_url():
        if Duotu555PageParser.classify_index_page_url_set:
            for url in Duotu555PageParser.classify_index_page_url_set:
                page = Duotu555PageDownloader.downPage(url)
                if page:
                    pageSoup = BeautifulSoup(page, 'html.parser', from_encoding="gb18030")
                    page_box_ul = pageSoup.find("ul", class_='img')
                    if page_box_ul:
                        page_box_ul_lis = page_box_ul.find_all('li')
                        if page_box_ul_lis:
                            for li in page_box_ul_lis:
                                a = li.find('a')
                                if a:
                                    beauty_page_url = a.get('href')
                                    print ("beauty_page_url %s" % (beauty_page_url))
                                    from image_url_handler import ImageUrlHandler
                                    ImageUrlHandler.add_page_url_to_queue(beauty_page_url)

                                    # p = li.find('p', class_='p_title')
                                    # if p:
                                    #     p_a = p.find('a')
                                    #     if p_a:
                                    #         a_title = p_a.text
                                    #         print ("beauty_page_url ttitle %s" % (a_title))


    # 获取美女主页大图url,并且将信息封装成ImageInfo对象
    # 比如获取https://www.duotu555.com/mm/32/35204.html页面中的大图
    @staticmethod
    def extract_page_content_img_url(page_Content):
        soupPage = BeautifulSoup(page_Content, 'html.parser', from_encoding="gb18030")
        imgs = soupPage.find_all('img', class_='tupian_img')
        if imgs:
            for img in imgs:
                url = img.get('src')
                img_info = img.attrs["alt"]
                print ("big image url :%s" %(url))
                image_info = ImageInfo(img_info, url, img_info, "https://www/duotu555.com")
                from image_url_handler import ImageUrlHandler
                ImageUrlHandler.for_download_imginfo_queue.put(image_info)


