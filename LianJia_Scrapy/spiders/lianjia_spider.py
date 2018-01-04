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
        house_id = response.xpath('//div[@class="brokerInfoText fr"]/div[@class="brokerName"]')
        house_header = response.xpath('//div[@class="title-wrapper"]/div[@class="content"]/div[@class="title"]')
        house_overview = response.xpath('//div[@class="overview"]/div[@class="content"]')
        house_main_content = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]')

        """     
            house_id = scrapy.Field()           # 房屋ID
            house_title = scrapy.Field()        # 房屋标题
            price = scrapy.Field()              # 总售价
            total_area = scrapy.Field()         # 总面积
            orientation = scrapy.Field()        # 方向
            community_name = scrapy.Field()     # 所在小区/社区
            price_per_area = scrapy.Field()     # 每平米价格
        """

        item['house_id'] = house_id.xpath('//a/@data-source-extends').extract()[0]
        print(item['house_id'])

        item['house_title'] = house_header.xpath('//h1/text()').extract()[0]
        print(item['house_title'])

        # item['name'] = house_main_content.xpath('//ul/li[1]/text()').extract()[0]
        item['price'] = house_overview.xpath('//div[@class="price "]/span/text()').extract()[0]
        print(item['price'])

        item['orientation'] = house_overview.xpath('//div[@class="houseInfo"]/div[@class="type"]/div[@class="mainInfo"]/text()').extract()[0]
        print(item['orientation'])

        item['total_area'] = house_overview.xpath('//div[@class="houseInfo"]/div[@class="area"]/div[@class="mainInfo"]/text()').extract()[0]
        print(item['total_area'])

        item['community_name'] = house_overview.xpath('//div[@class="aroundInfo"]/div[@class="communityName"]/a[@class="info "]/text()').extract()[0]
        print(item['community_name'])

        item['price_per_area'] = house_overview.xpath('//div[@class="price "]/div[@class="text"]/div[@class="unitPrice"]/span/text()').extract()[0]
        print(item['price_per_area'])

        yield item