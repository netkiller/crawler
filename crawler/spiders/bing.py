# -*- coding: utf-8 -*-
import scrapy


class BingSpider(scrapy.Spider):
    name = 'bing'
    allowed_domains = ['bing.com']
    start_urls = ['https://cn.bing.com/search?q=netkiller']

    def parse(self, response):
        for link in response.css('a::attr(href)'):
            # self.log('This url is %s' % link)
            yield {
                'url': link.css('a::attr(href)').extract()
                }

        next_page = response.css('a.sb_pagN::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        pass
