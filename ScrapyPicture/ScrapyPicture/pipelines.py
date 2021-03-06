# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class ScrapypicturePipeline(ImagesPipeline):
    #def process_item(self, item, spider):
    #    return item
    # 获取settings文件里设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        for p in range(2,51):
            image_url = item["pic_path"][:-5]+str(p)+'.jpg'
            image_referer = item["pic_url"][:-5]+'_'+str(p)+'.html'
            yield scrapy.Request(image_url,headers={'Referer': image_referer})


    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]

        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["pic_name"] +"_"+item["pic_no"]+ ".jpg")

        item["pic_path"] = self.IMAGES_STORE + "/" + item["pic_name"]

        return item
