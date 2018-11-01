#自动化测试工具爬取douyu
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ssl
from lxml import etree

class Douyu(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.num = 0
        self.count = 0
    def run(self):
        self.driver.get('https://www.douyu.com/directory/all')
#         print('当前直播人数',self.num)
#         print('当前观众人数',self.count)
        while True:
            html = self.driver.page_source
            content = etree.HTML(html)
            #print(html)
            numbers = content.xpath('//span[@class="dy-num fr"]/text()')
            names = content.xpath('//ul[@id="live-list-contentbox"]//h3[@class="ellipsis"]/text()')
#             print(len(names),len(numbers))
            
            for name,number in zip(names,numbers):
                name = name.strip()
                number = number.lstrip()
                print('观众人次',number,"\t",'房间名:',name)
                self.num+=1
                if number[-1] == '万':
                    number = number[:-1]
                    self.count +=int(float(number)*10000)
                else:
                    self.count +=int(number)
            time.sleep(1)
#             拖动到底部
#             js = "var q = document.documentElement.scrollTop=100000"
#             self.driver.execute_script(js)
            ret = self.driver.page_source.find('shark-pager-disable-next')
#             print('ret:',ret)
            if ret>=0:
                break
            self.driver.find_element_by_class_name('shark-pager-next').click()
            print('总直播人数',self.num)
            print('总观众人次',self.count)
        self.driver.quit()
# driver.get('https://www.douyu.com/directory/all')
# time.sleep(1)
# ret = driver.page_source.find('shark-pager-disable-next')
# print(ret)
if __name__=='__main__':
    douyu = Douyu()
    douyu.run()