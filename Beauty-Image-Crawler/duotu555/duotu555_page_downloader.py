#coding=utf-8
import requests
import traceback

class Duotu555PageDownloader:
    had_download_url_set = set()

    @staticmethod
    def downPage(url):
        if url in Duotu555PageDownloader.had_download_url_set:
            print ("page %s has been downloaded." %(url))
            return None
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print ("download page %s success ." %(url))
                page_content = response.content
                Duotu555PageDownloader.had_download_url_set.add(url)
                return page_content
        except Exception, e:
            print ("download page %s error due to %s" % (url, e.message))
            traceback.print_exc()

