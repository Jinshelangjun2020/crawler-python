#coding=utf-8
import requests
from pageparser import PageParser
from downloader import DownLoader

url = "https://www.meitulu.com/t/tuigirl/"

'''downLoader = DownLoader()'''
pageContent = DownLoader.downLoadPage(url)

'''爬虫入口'''
if len(pageContent):
    PageParser.parserForImageUrl(pageContent)




