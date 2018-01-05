# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ###################################################################################################
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

    ##################################################################################################
    ##################################################################################################


    pass
