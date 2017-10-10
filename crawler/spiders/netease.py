# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from crawler.items import CrawlerItem 

class NeteaseSpider(scrapy.Spider):
    name = 'netease'
    allowed_domains = ['money.163.com']
    start_urls = ['http://money.163.com']

    def parse(self, response):
        # Top 5
        # response.xpath('//ul[@class="topnews_nlist"]/li/h2/a/@href|//ul[@class="topnews_nlist"]/li/h3/a/@href').extract()
        for url in response.xpath('//ul[contains(@class,"topnews_nlist")]/li[@class="tpn_first"]/h2/a/@href|//ul[contains(@class,"topnews_nlist")]/li/h3/a/@href').extract():
            # self.log('URL: %s' % url)
            yield response.follow( url, callback=self.parse_item)
        
    def parse_item(self, response):
        l = ItemLoader(item=CrawlerItem(), response=response)
        l.add_xpath('title', '//div[@id="epContentLeft"]/h1/text()')
        l.add_xpath('ctime', '//div[@class="post_time_source"]/text()')
        l.add_xpath('description', '//div[@class="post_desc"]/text()')
        l.add_xpath('source', '//div[@class="post_time_source"]/a/text()')
        l.add_xpath('content', '//div[@id="endText"]')
        l.add_xpath('author', '//div[@class="ep-source cDGray"]/span[@class="left"]/text()')

        #l.add_value('ctime', time.strftime( '%Y-%m-%d %X', time.localtime() ))
        # l.add_value('content', response.body)
        return l.load_item()