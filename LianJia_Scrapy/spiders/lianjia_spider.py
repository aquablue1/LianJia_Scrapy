import scrapy
from scrapy.spider import Spider
from LianJia_Scrapy.items import LianjiaScrapyItem
from scrapy import Request
import ast
import re


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

        ## House identity location
        house_id = response.xpath('//div[@class="brokerInfoText fr"]/div[@class="brokerName"]')
        house_header = response.xpath('//div[@class="title-wrapper"]/div[@class="content"]/div[@class="title"]')

        ## House overview information and price information location
        house_overview = response.xpath('//div[@class="overview"]/div[@class="content"]')

        ## House detailed information location
        house_detailed_info = response.xpath('//div[@class="m-content"]//div[@class="introContent"]/div[@class="base"]'
                                             '/div[@class="content"]/ul')
        # print(house_detailed_info.extract())

        ## House trade information location
        house_trade_info = response.xpath('//div[@class="m-content"]//div[@class="introContent"]/div[@class="transaction"]'
                                          '/div[@class="content"]/ul')
        # print(house_trade_info.extract())

        """     
            ## House Identity
            house_id = scrapy.Field()           # 房屋ID
            house_title = scrapy.Field()        # 房屋标题
        
            ## House price information
            price = scrapy.Field()              # 总售价
            first_price = scrapy.Field()        # 最低首付
            tax = scrapy.Field()                # 税费
            price_per_area = scrapy.Field()     # 每平米价格
        
            ## House overview information
            total_area = scrapy.Field()         # 总面积
            orientation = scrapy.Field()        # 方向
            house_structure = scrapy.Field()    # 房屋结构
            community_name = scrapy.Field()     # 所在小区/社区
            house_location = scrapy.Field()     # 房屋所在区域
        
            ## House detailed information
            house_structure_detailed = scrapy.Field()       # 具体户型信息
            inside_area = scrapy.Field()                    # 套内面积
            declaration_status = scrapy.Field()             # 装修情况
            is_elevator = scrapy.Field()                    # 配备电梯
            floor = scrapy.Field()                          # 所在楼层
            house_type = scrapy.Field()                     # 户型结构 (注意区分house_structure，房屋结构)
            building_type = scrapy.Field()                  # 建筑类型
            building_structure = scrapy.Field()             # 建筑结构
            elevator_per_house = scrapy.Field()             # 梯户比例
            property_year = scrapy.Field()                  # 产权年限
        
            ## House trade information
            start_sale_date = scrapy.Field()                # 挂牌时间
            last_sale_date = scrapy.Field()                 # 上次交易时间
            trade_gap = scrapy.Field()                      # 房屋年限（据上次交易年限）
            pledge_info = scrapy.Field()                    # 抵押信息
            trade_ownership = scrapy.Field()                # 交易权限
            house_purpose = scrapy.Field()                  # 房屋用途
            property_ownership = scrapy.Field()             # 产权所属
            ownership_certificate = scrapy.Field()          # 房本备件
        """

        ## House identity extract =========================================================
        # House ID is stored in a dict-liked string. therefore, convert the string to dict object first.
        # and then extract the house id based on key='house_code'

        house_id_dict = house_id.xpath('//a/@data-source-extends').extract()[0]
        house_id_dict = ast.literal_eval(house_id_dict)
        item['house_id'] = house_id_dict['house_code']

        item['house_title'] = house_header.xpath('//h1/text()').extract()[0]

        print(item['house_id'])
        print(item['house_title'])

        ## House price information extract ================================================
        item['price'] = float(house_overview.xpath('//div[@class="price "]/span/text()').extract()[0])

        first_price_str = house_overview.xpath(
            '//div[@class="price "]/div[@class="text"]/div[@class="tax"]/span[@class="taxtext"]/span[1]/text()').extract()[0]
        item['first_price'] = float(re.findall('\d+', first_price_str)[0])

        item['tax'] = float(house_overview.xpath(
            '//div[@class="price "]/div[@class="text"]/div[@class="tax"]/span[@class="taxtext"]//span[@id="PanelTax"]/text()').extract()[0])

        item['price_per_area'] = float(house_overview.xpath(
            '//div[@class="price "]/div[@class="text"]/div[@class="unitPrice"]/span/text()').extract()[0])

        print(item['price'])
        print(item['first_price'])
        print(item['tax'])
        print(item['price_per_area'])

        ## House overview information extract ============================================
        total_area_str = house_overview.xpath(
            '//div[@class="houseInfo"]/div[@class="area"]/div[@class="mainInfo"]/text()').extract()[0]
        item['total_area'] = float(re.findall('\d+', total_area_str)[0])

        item['orientation'] = house_overview.xpath(
            '//div[@class="houseInfo"]/div[@class="type"]/div[@class="mainInfo"]/text()').extract()[0]

        item['house_structure'] = house_overview.xpath(
            '//div[@class="houseInfo"]/div[@class="room"]/div[@class="mainInfo"]/text()').extract()[0]

        item['community_name'] = house_overview.xpath(
            '//div[@class="aroundInfo"]/div[@class="communityName"]/a[@class="info "]/text()').extract()[0]

        item['house_location'] = house_overview.xpath(
            '//div[@class="aroundInfo"]/div[@class="areaName"]/a[@class="supplement"]/text()').extract()[0]

        print(item['total_area'])
        print(item['orientation'])
        print(item['house_structure'])
        print(item['community_name'])
        print(item['house_location'])

        ## House detailed information ======================================================
        item['house_structure_detailed'] = house_detailed_info.xpath('.//li[1]/text()').extract()[0]

        inside_area_str = house_detailed_info.xpath('.//li[5]/text()').extract()[0]
        item['inside_area'] = float(re.findall('\d+', inside_area_str)[0])

        item['declaration_status'] = house_detailed_info.xpath('.//li[9]/text()').extract()[0]

        item['is_elevator'] = house_detailed_info.xpath('.//li[11]/text()').extract()[0]

        item['floor'] = house_detailed_info.xpath('.//li[2]/text()').extract()[0]

        item['house_type'] = house_detailed_info.xpath('.//li[4]/text()').extract()[0]

        item['building_type'] = house_detailed_info.xpath('.//li[6]/text()').extract()[0]

        item['building_structure'] = house_detailed_info.xpath('.//li[8]/text()').extract()[0]

        item['elevator_per_house'] = house_detailed_info.xpath('.//li[10]/text()').extract()[0]

        item['property_year'] = house_detailed_info.xpath('.//li[12]/text()').extract()[0]

        print(item['house_structure_detailed'])
        print(item['inside_area'])
        print(item['declaration_status'])
        print(item['is_elevator'])
        print(item['floor'])
        print(item['house_type'])
        print(item['building_type'])
        print(item['building_structure'])
        print(item['elevator_per_house'])
        print(item['property_year'])

        ## House trade information =========================================================
        item['start_sale_date'] = house_trade_info.xpath('.//li[1]/text()').extract()[0]

        item['last_sale_date'] = house_trade_info.xpath('.//li[3]/text()').extract()[0]

        item['trade_gap'] = house_trade_info.xpath('.//li[5]/text()').extract()[0]

        item['pledge_info'] = house_trade_info.xpath('.//li[7]/span[2]/text()').extract()[0]

        item['trade_ownership'] = house_trade_info.xpath('.//li[2]/text()').extract()[0]

        item['house_purpose'] = house_trade_info.xpath('.//li[4]/text()').extract()[0]

        item['property_ownership'] = house_trade_info.xpath('.//li[6]/text()').extract()[0]

        item['ownership_certificate'] = house_trade_info.xpath('.//li[8]/text()').extract()[0]

        print(item['start_sale_date'])
        print(item['last_sale_date'])
        print(item['trade_gap'])
        print(item['pledge_info'])
        print(item['trade_ownership'])
        print(item['house_purpose'])
        print(item['property_ownership'])
        print(item['ownership_certificate'])


        yield item

