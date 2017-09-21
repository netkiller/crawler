# -*- coding: utf-8 -*-
import scrapy


class NetkillerSpider(scrapy.Spider):
    name = 'netkiller'
    allowed_domains = ['netkiller.cn']
    start_urls = ['http://www.netkiller.cn/']

    def parse(self, response):
        for link in response.xpath('//div[@class="blockquote"]')[1].css('a.ulink'):
            # self.log('This url is %s' % link)
            yield {
                'name': link.css('a::text').extract(),
                'url': link.css('a.ulink::attr(href)').extract()
                }
       
        pass
