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
#B站有评论的页面
SPIDER_URL = 'https://www.bilibili.com/bangumi/play/ss25681'
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
        self.cou = 0        #总条数计数器
        self.fcou = 0       #for循环条数计数器
    def run(self):
        #读取加载url
        self.driver.get(SPIDER_URL)   
        #等待浏览器加载完成         
        self.driver.implicitly_wait(3)
        #拉到底下获取评论
        js = "var q = document.documentElement.scrollTop=1000000"  
        self.driver.execute_script(js)  
        while True:     
            time.sleep(1)
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
                #写入文件
                self.sheet.write(self.cou+j+1,0,textCount.text)
                self.sheet.write(self.cou+j+1,1,name.text)
                self.sheet.write(self.cou+j+1,2,commonTime.text)
                self.sheet.write(self.cou+j+1,3,text.text)
                self.sheet.write(self.cou+j+1,4,showGood.text)
                self.fcou = j
                print(textCount.text);print(name.text);print(commonTime.text);print(text.text);print(showGood.text)
                #print(j)
            #print(name.__len__() ,text.__len__() ,textCount.__len__() ,commonTime.__len__(),showGood.__len__())
            self.cou += self.fcou
            try:
                self.driver.find_element_by_xpath('//div[@class="header-page paging-box"]/a[@class="next"]').click()
            except:
                break
            self.count += 1
            if self.count == MAXPAGE_SIZE:
                print(self.cou)
                break
        self.book.save("bili2.xls")
        print("end")
if __name__=='__main__':
    bili = Bilibili()
    bili.run()