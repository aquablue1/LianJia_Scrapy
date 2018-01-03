# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # name of house
    name = scrapy.Field()

    # price of house
    price = scrapy.Field()

    # total area of ahouse
    total_area = scrapy.Field()

    pass
