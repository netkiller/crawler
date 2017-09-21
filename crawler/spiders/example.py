# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from crawler.items import CrawlerItem 
import time

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['netkiller.cn']
    start_urls = ['https://netkiller.cn/java/index.html']
    def parse(self, response):

        item_selector = response.xpath('//a/@href')
        for url in item_selector.extract():
            if 'html' in url.split('.'):
                url = response.urljoin(url)
                yield response.follow( url, callback=self.parse_item)

        next_page = response.xpath('//a[@accesskey="n"]/@href').extract_first()
        self.log('Next page: %s' % next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)   
        
    def parse_item(self, response):
        l = ItemLoader(item=CrawlerItem(), response=response)
        l.add_css('title', 'title::text')
        l.add_value('ctime', time.strftime( '%Y-%m-%d %X', time.localtime() ))
        # l.add_value('content', response.body)
        return l.load_item()