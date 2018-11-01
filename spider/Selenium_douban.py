from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ssl
from lxml import etree
class Douban(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.num = 0
        self.count = 0
    def run(self):
        self.driver.get('https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')
        for i in range(2):
            js = "var q = document.documentElement.scrollTop=1000000"
            self.driver.execute_script(js)
            time.sleep(1)
        html = self.driver.page_source
        content = etree.HTML(html) 
        print(html)#//div//div[@class="movie-content"]/a
        names = content.xpath('/html/body/div[3]/div[1]/div/div[1]/div[6]/div/div/div/div/span/a/text()')#用xPath Finder
        print(names)
if __name__=='__main__':
    douban = Douban()
    douban.run()