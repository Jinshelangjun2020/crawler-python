#coding=utf-8
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from queue import Queue
import threading
from bs4 import BeautifulSoup

class ImageUrlHandler:
    #主页box区域的美女主页列表集合url队列,比如 https://www.duotu555.com/mm/32/35204.html 这样的美女主页的url队列
    box_beauty_page_url_queue = Queue(maxsize=0)
    #要下载的图片信息队列
    for_download_imginfo_queue = Queue(maxsize=0)

    @staticmethod
    def add_page_url_to_queue(url):
        ImageUrlHandler.box_beauty_page_url_queue.put(url)

    @staticmethod
    def add_download_imginfo_queue(image_info):
        ImageUrlHandler.for_download_imginfo_queue.put(image_info)

    # 获取子页面的分类列表页URL
    @staticmethod
    def pageUrlQueueWork():
        print ("pageUrlQueueWork ...")
        while 1:
            if not ImageUrlHandler.box_beauty_page_url_queue.empty():
                page_url = ImageUrlHandler.box_beauty_page_url_queue.get()
                # 从美女主页下载美女大图
                if page_url:
                    print ("begin to download page %s" % (page_url))
                    # 下载该网页
                    from duotu555_page_downloader import Duotu555PageDownloader
                    page_content = Duotu555PageDownloader.downPage(page_url)

                    from duotu555_page_parser import Duotu555PageParser
                    Duotu555PageParser.extract_page_content_img_url(page_content)

                    page_url_prefix_arr = page_url.rpartition("/")
                    page_url_prefix = ""
                    if page_url_prefix_arr:
                        page_url_prefix = page_url_prefix_arr[0]

                    #todo 抽取foot
                    foot_soup = BeautifulSoup(page_content, 'html.parser', from_encoding="gb18030")
                    if foot_soup:
                        foot_div = foot_soup.find(attrs={'id': 'pages'})
                        if foot_div:
                            girlPages = foot_div.find_all('a')
                            for page in girlPages:
                                subImgUrl = page.get('href')
                                sub_foot_page_url = page_url_prefix + "/" + subImgUrl
                                print("sub tuigirl image url %s" % (sub_foot_page_url))
                                ImageUrlHandler.add_page_url_to_queue(sub_foot_page_url)
            else:
                sleep(5)
                continue

    @staticmethod
    def imginfoQueueWork():
        print ("imginfoQueueWork ...")
        while 1:
            if not ImageUrlHandler.for_download_imginfo_queue.empty():
                imageInfo = ImageUrlHandler.for_download_imginfo_queue.get()
                if imageInfo:
                    print ("begin to download image %s" % (imageInfo.url))
                    # 下载该图片
            else:
                sleep(1)
                continue

    @staticmethod
    def start():
        threads = []
        t1 = threading.Thread(target=ImageUrlHandler.pageUrlQueueWork)
        threads.append(t1)
        t2 = threading.Thread(target=ImageUrlHandler.imginfoQueueWork)
        threads.append(t2)

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # print ("ImageUrlHandler start ...")
        # with ThreadPoolExecutor(3) as executor:
        #     executor.submit(ImageUrlHandler.pageUrlQueueWork())
        # print ("ThreadPoolExecutor pageUrlQueueWork start ...")
        #
        # with ThreadPoolExecutor(3) as executor2:
        #     executor2.submit(ImageUrlHandler.imginfoQueueWork())
        # print ("ThreadPoolExecutor imginfoQueueWork start ...")
