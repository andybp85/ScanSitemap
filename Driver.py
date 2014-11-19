'''
Created on Jul 14, 2014

@author: Andrew Stanish
'''
from scansitemap import Scanner

def main():
    scan = Scanner('http://landmarqtreeservice.com/sitemap/','page')
    scan.run()

if __name__ == '__main__':
    main()