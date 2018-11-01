# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
class TencenthrPipeline(object):
    # 初始化
    def __init__(self):
        self.filename = open('tencenthr.json', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        json_str = json.dumps(dict(item)) + '\n'
        content = json_str.encode('utf-8')
        self.filename.write(str(content, encoding='utf-8'))
        return item

    def close_spider(self, spider):
        self.filename.close()

