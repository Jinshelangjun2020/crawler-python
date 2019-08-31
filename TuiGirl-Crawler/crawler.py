#coding=utf-8
import requests
from pageparser import PageParser
from downloader import DownLoader

url = "https://www.meitulu.com/t/tuigirl/"

'''downLoader = DownLoader()'''
pageContent = DownLoader.downLoadPage(url)

if len(pageContent):
    PageParser.parserForImageUrl(pageContent)




