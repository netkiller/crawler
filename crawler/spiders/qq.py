# -*- coding: utf-8 -*-
import scrapy


class QqSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['finance.qq.com']
    start_urls = ['http://finance.qq.com/']

    def parse(self, response):
        response.xpath('//div[@class="qq_article"]/div[@class="hd"]/h1/text()').extract()
        response.xpath('//span[@class="a_time"]/text()').extract()
        response.xpath('//span[@class="a_source"]/text()').extract()
        response.xpath('//div[@id="Cnt-Main-Article-QQ"]').extract()
        pass
