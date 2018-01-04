# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    house_id = scrapy.Field()           # 房屋ID
    house_title = scrapy.Field()        # 房屋标题
    price = scrapy.Field()              # 总售价
    total_area = scrapy.Field()         # 总面积
    orientation = scrapy.Field()        # 方向
    community_name = scrapy.Field()     # 所在小区/社区
    price_per_area = scrapy.Field()     # 每平米价格

    pass
