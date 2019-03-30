import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        f = open("the_urls.txt", "a")
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            f.write("\n" + url)
                        
        f.close()
                
        # open and read the file after write and appending contents in it.
        f = open("the_urls.txt", "r")
        print(f.read())



scrape = Scraper('https://news.google.com')
scrape.scrape()
