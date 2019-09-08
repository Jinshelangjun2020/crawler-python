from duotu555_page_parser import Duotu555PageParser
from duotu555_page_downloader import Duotu555PageDownloader
from image_url_handler import ImageUrlHandler

import sys
reload(sys)
sys.setdefaultencoding('utf8')

Duotu555PageParser.parserPage(Duotu555PageDownloader.downPage("https://www.duotu555.com"))
ImageUrlHandler.start()
