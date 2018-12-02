from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ssl
from lxml import etree
import re
import xlwt
from xlrd import *
from xlutils.copy import copy
from datetime import datetime
#爬取最大的页数，0就是全爬完
MAXPAGE_SIZE = 0
#用于开始加载页数 0为不用
PAGE_START = 2995
#每次请求间隔时间,越小越快，但不稳定  0.3在700页左右断过一次 0.4在577页停过一次  0.2在157 最好0.5
REFRESH_WAIT_TIME = 0.5
#B站有评论的页面
SPIDER_URL = 'https://www.bilibili.com/bangumi/play/ss21542'                      #https://www.bilibili.com/bangumi/play/ss25681  25510  GG 3450停掉了超出xls大小了
class Bilibili(object):
    def __init__(self):
        #创建工作簿
        self.book = xlwt.Workbook()               
        #创建sheet
        self.sheet = self.book.add_sheet(u'sheet',cell_overwrite_ok=True)
        #创建浏览器驱动
        self.driver = webdriver.Chrome()
        self.count = 0
        #写入第一行
        self.sheet.write(0,0,"评论id")
        self.sheet.write(0,1,"昵称")
        self.sheet.write(0,2,"时间")
        self.sheet.write(0,3,"评论")
        self.sheet.write(0,4,"点赞数")
        self.sheet.write(0,5,"客户端")
        self.countSum = 0        #总条数计数器
        self.forCount = 0       #for循环条数计数器
        #读取加载url
        self.driver.get(SPIDER_URL)   
    def run(self):
              
        #等待浏览器加载完成         
        self.driver.implicitly_wait(10)
        #拉到底下获取评论
        js = "var q = document.documentElement.scrollTop=1000000"  
        self.driver.execute_script(js)  
        while True:     
            time.sleep(REFRESH_WAIT_TIME)
            html = self.driver.page_source
            #去掉换行标签符（没有效果）
            htm = ((html.replace('<br>','')).replace('</br>','')).replace('\n','')
            #print(htm)
            content = etree.HTML(htm)
            #etree.ElementTree(content).write("text.xml", pretty_print=True)
            #下面这个xpath有问题，爬出的对象都是全部的评论块，数量还等于评论块数
            commons = content.xpath('//span[@class="floor"]/../..')
            print(commons)
            for j,i in enumerate(commons):
                #print(i.text)
                #name=text=textCount=commonTime=showGood = ""
                name = i.xpath('//span[@class="floor"]/../preceding-sibling::div[1]/a')[(j-1)*2+2]
                text =  i.xpath('//p[@class="text"]')[j]
                textCount = i.xpath('//span[@class="floor"]')[j]
                commonTime = i.xpath('//span[@class="floor"]/following-sibling::span[@class="time"]')[j]
                showGood = i.xpath('//span[@class="floor"]/following-sibling::span[@class="like"]/span|//span[@class="floor"]/following-sibling::span[@class="like "]/span')[j]
                client = i.xpath('//span[@class="floor"]/following-sibling::span[1]')[j]
                clentL = ''
                if '来自' in client.text:
                    clentL = client.xpath('./a/text()')
#                 if '回复' in client.text:
#                     client.text = '无'
                #写入文件
                self.sheet.write(self.countSum+j+1,0,textCount.text)
                self.sheet.write(self.countSum+j+1,1,name.text)
                self.sheet.write(self.countSum+j+1,2,commonTime.text)
                self.sheet.write(self.countSum+j+1,3,text.text)
                self.sheet.write(self.countSum+j+1,4,showGood.text)
                self.sheet.write(self.countSum+j+1,5,clentL)
                self.forCount = j
                print(client.text);print(textCount.text);print(name.text);print(commonTime.text);print(text.text);print(showGood.text)
                #print(j)
            #print(name.__len__() ,text.__len__() ,textCount.__len__() ,commonTime.__len__(),showGood.__len__())
            self.countSum += self.forCount
            try:
                self.driver.find_element_by_xpath('//div[@class="bottom-page paging-box-big"]/a[@class="next"]').click()
            except:
                break
            self.count += 1
            if self.count == MAXPAGE_SIZE:
                print(self.countSum)
                break
        self.book.save("bili-紫罗兰永恒花园2.xls")
        print("end")
    def reload(self):
        self.driver.implicitly_wait(10)
        js = "var q = document.documentElement.scrollTop=1000000"  
        self.driver.execute_script(js)  
#         self.driver.find_element_by_xpath('//div[@class="page-jump"]/input').click()
        self.driver.find_element_by_xpath('//div[@class="page-jump"]/input').send_keys(PAGE_START);
        self.driver.find_element_by_xpath('//div[@class="page-jump"]/input').send_keys(Keys.ENTER)
        time.sleep(3)
if __name__=='__main__':
    bili = Bilibili()
    if PAGE_START != 0:
        bili.reload()
    bili.run()