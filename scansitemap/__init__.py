'''
Created on Jun 24, 2014

@author: Andrew Stanish

'''


import time, Queue
from threading import BoundedSemaphore

from scansitemap.sitemap import Sitemap
from scansitemap.threadpage import ThreadPage


class Scanner(object):

    btime = time.time()
    tcount = []

    def __init__(self, sitemapurl, divID, maxconnections=10, outfile=False):
        self.maxconnections = maxconnections
        print 'max concurrent connections: ' + str(self.maxconnections)
        self.sitemap = Sitemap(sitemapurl)
        print 'Sitemap opened ' + str(time.time() - self.btime)
        self.sitemap.getLinks(divID)
        self.outf = open(outfile) if outfile else False

    def run(self):

        queue = Queue.Queue()
        pool_sema = BoundedSemaphore(value=self.maxconnections)

        for l in self.sitemap.links:
            t = ThreadPage(queue, self.tcount, pool_sema, self.outf)
            t.setDaemon(True)
            t.start()
            queue.put(l)
        queue.join()

        if self.outf:
            self.outf.close()

        print 'done: ' + str(time.time() - self.btime) + " pages checked: " + str(len(self.tcount))
