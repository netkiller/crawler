# -*- coding: utf-8 -*-
import scrapy


class SohuSpider(scrapy.Spider):
    name = 'sohu'
    allowed_domains = ['sohu.com']
    start_urls = ['http://sohu.com/']

    def parse(self, response):
        response.xpath('//div[@class="text-title"]/h1/text()[1]').extract()
        response.xpath('//span[@class="time" and @id="news-time"]/text()').extract()
        response.xpath('//article[@class="article"]').extract()
        response.xpath('//h4/a/text()').extract()

        pass
