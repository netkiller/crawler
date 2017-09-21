# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['netkiller.cn']
    start_urls = ['https://netkiller.cn/linux/index.html']

    def parse(self, response):
        yield {'title': response.css('title::text').extract()}

        filename = '/tmp/%s' % response.url.split("/")[-1]

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        next_page = response.xpath('//a[@accesskey="n"]/@href').extract_first()
        self.log('Next page: %s' % next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)    

        pass
