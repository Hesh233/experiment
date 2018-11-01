import scrapy
from tencenthr.items import TencenthrItem
class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPostion'
    allowed_domains =['tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]
    def parse(self,response):
       content = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
       for i in content:
           list = []
           item = TencenthrItem()
           item['positionname']=i.xpath('./td/a/text()').extract()[0]
           item['posititonlink']=i.xpath('./td/a/@href').extract()[0]
           if len(i.xpath('./td[2]/text()').extract())>0:
               item['posititonType']=i.xpath('./td[2]/text()').extract()[0]
           else:item['posititonType']=''
           item['posititonNum']=i.xpath('./td[3]/text()').extract()[0]
           item['workLocation']=i.xpath('./td[4]/text()').extract()[0]
           item['publishtime']=i.xpath('./td[5]/text()').extract()[0]
           print(item)
           if self.offset <=3010:
               self.offset +=10
               print(self.offset,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
           yield item
           yield scrapy.Request(self.url+str(self.offset),callback = self.parse)