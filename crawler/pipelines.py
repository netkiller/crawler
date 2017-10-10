# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem

class CrawlerPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.json', 'w')
        self.lst = open('news.lst', 'w')

    def close_spider(self, spider):
        self.file.close()
        self.lst.close()
    def process_item(self, item, spider):
        if item != None:
        # self.log("PIPE: %s" % item.title)
            self.lst.write(str(item['title']) + "\n")
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)   
            return item
        else:
            raise DropItem("Missing price in %s" % item)
    
