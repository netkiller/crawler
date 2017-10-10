# -*- coding: utf-8 -*-
import scrapy


class IfengSpider(scrapy.Spider):
    name = 'ifeng'
    allowed_domains = ['finance.ifeng.com']
    start_urls = ['http://finance.ifeng.com/']

    def parse(self, response):
        # 标题 response.xpath('//div[@id="artical"]/h1[@id="artical_topic"]/text()').extract()
        # 时间 response.xpath('//*[@id="artical_sth"]/p/span[@class="ss01"]/text()').extract()
        # 来源 response.xpath('//*[@id="artical_sth"]/p/span/span[@class="ss03"]/text()').extract()
        # 内容 response.xpath('//div[@id="artical"]//div[@id="main_content"]').extract()
        # 作者 response.xpath('//div[@id="artical"]//div[@id="artical_sth2"]/p[@class="iphone_none"][1]/text()').extract()
        pass
