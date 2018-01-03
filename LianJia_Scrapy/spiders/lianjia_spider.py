import scrapy
from scrapy.spider import Spider
from LianJia_Scrapy.items import LianjiaScrapyItem
from scrapy import Request



class LianJiaSpider(Spider):
    # Spider name
    name = "lianjia_house"

    # HTTPS Request Header
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    }

    # Set root url and headers
    def start_requests(self):
        url = 'https://nj.lianjia.com/ershoufang/103101077336.html'
        yield Request(url, headers=self.headers)

    # Do scrapy.
    def parse(self, response):
        item = LianjiaScrapyItem()
        # house_info = response.xpath('//div[@class="introContent"]/div')

        item['name'] = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[1]/text()').extract()[0]
        item['price'] = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[2]/text()').extract()[0]
        item['total_area'] = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[3]/text()').extract()[0]

        yield item