'''
Created on Jul 13, 2014

@author: Andrew Stanish
'''
import time
from threading import Thread
from mechanize import Browser

from scansitemap.sitemap import Sitemap

class ThreadPage(Thread):

    def __init__(self, queue, tcount, pool_sema, outfile=False):
        Thread.__init__(self)
        self.queue = queue
        self.count = tcount
        self.btime = time.time()
        self.pool = pool_sema
        self.outf = outfile if outfile else False
        self.sitemap = Sitemap()

    def run(self):
        while True:
            br = Browser()
            addr = self.queue.get()

            self.count.append(addr['href'])
            self.pool.acquire()
            stime = time.time()
            try:
                self.sitemap.load(addr['href'])
                print 'success: ' + self.sitemap.page.title.string + ' ' + str(time.time() - stime)
            except Exception as inst:
                print 'FAIL: ' + str(inst) + ' : ' + addr['href'] + ' ' + str(time.time() - stime)
                if self.outf:
                    self.outf.write('FAIL: ' + str(inst) + ' : ' + addr['href'] + ' ' + str(time.time() - stime))
            self.pool.release()