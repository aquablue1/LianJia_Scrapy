# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
from MySQLdb import cursors
# import codecs
import copy
from scrapy.utils.project import get_project_settings


class LianjiaScrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class lianjia_pipeline(object):

    def __init__(self):
        # Methods_1: use the database info defined in settings file.
        # self.settings = get_project_settings()
        # self.settings["MYSQL_HOST"] = 'localhost'
        self.db = MySQLdb.connect(host='127.0.0.1',
                                  db='lianjia_house',
                                  user='user1',
                                  passwd='1212',
                                  cursorclass=cursors.DictCursor,
                                  charset='utf8',
                                  use_unicode=False)

    def process_item(self, item, spider):
        cursor = self.db.cursor()

        status = self.conditional_insert(cursor, item)

        # 输入完指令之后，一定要记得commit
        self.db.commit()

        return item

    def conditional_insert(self, tx, item):
        """

        :param tx:
        :param item:
        :return:
        """
        sql_insert = "insert into nanjing_statistics(" \
                     "house_id, house_title, " \
                     "price, first_price, tax, price_per_area, " \
                     "total_area, orientation, house_structure, community_name, house_location, " \
                     "house_structure_detailed, inside_area, declaration_status, is_elevator, floor, house_type, " \
                     "building_type, building_structure, elevator_per_house, property_year, " \
                     "start_sale_date, last_sale_date, trade_gap, pledge_info, trade_ownership, house_purpose, " \
                     "property_ownership, ownership_certificate) values(" \
                     "%s, %s, " \
                     "%s, %s, %s, %s, " \
                     "%s, %s, %s, %s, %s," \
                     "%s, %s, %s, %s, %s, %s, " \
                     "%s, %s, %s, %s, " \
                     "%s, %s, %s, %s, %s, %s, " \
                     "%s, %s) "

        """     
            house_id = scrapy.Field()           # 房屋ID
            house_title = scrapy.Field()        # 房屋标题
            price = scrapy.Field()              # 总售价
            total_area = scrapy.Field()         # 总面积
            orientation = scrapy.Field()        # 方向
            community_name = scrapy.Field()     # 所在小区/社区
            price_per_area = scrapy.Field()     # 每平米价格
        """
        params = (item["house_id"], item["house_title"],
                  item["price"], item['first_price'], item["tax"], item["price_per_area"],
                  item['total_area'], item["orientation"], item['house_structure'], item["community_name"],item['house_location'],
                  item['house_structure_detailed'], item['inside_area'], item['declaration_status'], item['is_elevator'],
                  item['floor'], item['house_type'],
                  item['building_type'], item['building_structure'], item['elevator_per_house'], item['property_year'],
                  item['start_sale_date'],item['last_sale_date'], item['trade_gap'], item['pledge_info'],
                  item['trade_ownership'], item['house_purpose'],
                  item['property_ownership'], item['ownership_certificate'])

        try:
            tx.execute(sql_insert, params)

        except  MySQLdb.IntegrityError:
            print("Duplicated KEY VALUE error!")
            return False

        return True

    def _handle_error(self, failue, item, spider):
        print(failue)