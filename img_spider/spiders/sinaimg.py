# -*- coding: utf-8 -*-
import scrapy

from img_spider.items import ImgSpiderItem


class SinaimgSpider(scrapy.Spider):
    name = 'sinaimg'
    allowed_domains = ['sina.com']
    start_urls = ['http://slide.news.sina.com.cn/z/slide_1_64237_371026.html#p=4']

    def parse(self, response):
        dir_name = '一楼一武林'
        img_urls = response.xpath('//div[@class="scroll-item"]/div[@class="img-wrap"]//img/@data-src').extract()
        item = ImgSpiderItem()
        item['dir_name'] = dir_name
        item['img_urls'] = img_urls
        yield item
