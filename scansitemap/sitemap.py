'''
Created on Jul 13, 2014

@author: Andrew Stanish
'''
import time
from bs4 import BeautifulSoup
from mechanize import Browser

class Sitemap(object):
    '''

    This class opens a sitemap and defines the operations possible.

    '''

    br = Browser()

    def __init__(self, url=False):
        self.page = BeautifulSoup(self.br.open(url)) if url else False


    def load(self,url):
        self.page = BeautifulSoup(self.br.open(url))

    def getLinks(self, divID, ulNum=0):
        sitemap_div = self.page.find('div', id=divID)
        self.links = sitemap_div.find_all('ul')[ulNum].find_all('a')
        print str(len(self.links)) + ' links obtained '
