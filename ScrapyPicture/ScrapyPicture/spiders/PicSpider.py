import scrapy
from ScrapyPicture import items
import datetime


class PicSpider(scrapy.Spider):
    name = 'btfspider'
    allowed_domains = ['mm131.com']

    offset = 1
    url = "http://www.mm131.com/xinggan"

    start_urls = [url]

    def parse(self, response):

        base_pic_list = response.xpath('//dl[@class="list-left public-box"]/dd')

        no = 2
        for each in base_pic_list[1:-2]:
            item = items.ScrapypictureItem()
            item["pic_name"] = each.xpath('./a/text()').extract()[0]
            item["pic_path"] = each.xpath('./a/img/@src').extract()[0]
            item["pic_url"] = each.xpath('./a/@href').extract()[0]
            item["pic_no"] = str(no)
            no +=1
            yield item

        self.offset += 1
        yield scrapy.Request(self.url + '/list_6_'+str(self.offset)+'.html', callback = self.parse)