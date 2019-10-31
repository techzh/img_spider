# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from img_spider.items import ImgSpiderItem


class ImgSpiderPipeline(object):
    def process_item(self, item, spider):
        pass

class SinaImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item, ImgSpiderItem):
            if item['img_urls']:
                for img_url in item['img_urls']:
                    img_name = img_url.split('/')[-1]
                    yield Request(img_url, meta={'dir_name':item['dir_name'],'img_name':img_name})

    def file_path(self, request, response=None, info=None):
        # base_dir = '/Users/zhangyafeng1/work/workspace/workfile/imgs'
        dir_name = request.meta['dir_name']
        img_name = request.meta['img_name']
        dir_name = re.sub(r'[?\\*|"<>:/]', '', dir_name)
        file_name = u'{0}/{1}'.format(dir_name, img_name)
        return file_name