import scrapy
from scrapy.spider import Spider
from LianJia_Scrapy.items import LianjiaScrapyItem
from scrapy import Request
import ast
import re
import MySQLdb

class LianJiaSpider(Spider):
    # Spider name
    name = "lianjia_url_spider"

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
        urls = ['https://nj.lianjia.com/ershoufang/pg1/']
        for url in urls:
            yield Request(url, headers=self.headers)

    # Do scrapy.
    def parse(self, response):
        """
        " extract house url information from the url given in start_request methods
        " Then store all results to TABLE(nanjing_house_urls) in lianjia_house database.
        " Later work should seperate the database connecting module to a seperated place.
        :param response:
        :return:
        """
        dbparams = dict(
            host="localhost",
            db="lianjia_house",
            user="user1",
            passwd="1212",
            charset="utf8",
            # cursorclass=cursors.DictCursor,
            use_unicode=False,
        )
        db = MySQLdb.connect(**dbparams)

        # first locate all urls:
        url_location = response.xpath('//div[@class="content "]//ul[@class="sellListContent"]/li[@class="clear"]')
        # print(url_location.extract()[0])
        for url_loct in url_location:
            url = url_loct.xpath('.//a/@href').extract()[0]
            print(str(url))
            cursor = db.cursor()
            sql = 'insert into nanjing_house_urls (url) values (\'' + url + '\')'

            try:
                cursor.execute(sql)
                db.commit()
            except  MySQLdb.IntegrityError:
                print("Duplicated KEY VALUE error!")

        next_url_location = '//div[@class="contentBottom clear"]//div[@class="page-box house-lst-page-box"]/@page-data'
        next_url_dict_str = response.xpath(next_url_location).extract()
        # print(next_url_location)
        # print(next_url_dict_str[0])

        url_id_dict = ast.literal_eval(next_url_dict_str[0])
        last_page = url_id_dict['totalPage']
        cur_page = url_id_dict['curPage']
        if(cur_page < last_page):
            next_url = 'https://nj.lianjia.com/ershoufang/pg' + str(cur_page+1) + '/'
            print(next_url)
            yield Request(next_url, headers=self.headers)
        else:
            print("********** END OF COLLECTION ***********")



