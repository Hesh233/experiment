# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencenthrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionname = scrapy.Field()
    posititonlink = scrapy.Field()
    posititonType = scrapy.Field()
    posititonNum = scrapy.Field()
    workLocation = scrapy.Field()
    publishtime = scrapy.Field()
    
