#coding=utf-8

import MySQLdb

# In order to show chinese correct, set the charset as utf8 is essential.
# charset='utf8'
"""
python27环境下使用
import sys
reload(sys)
sys.setdefaultencoding('utf8')
但在python36下，reload()被取消，无法进行累死操作。
"""
db = MySQLdb.connect("localhost", "user1", "1212", "lianjia_house", charset='utf8')

cursor = db.cursor()

# cursor.execute('SET NAMES gbk')

view_all = "SELECT * FROM nanjing_statistics"

cursor.execute(view_all)

data = cursor.fetchall()

for row in data:
    house_id = row[0]
    house_title = row[1]
    price = row[2]
    total_area = row[3]
    orientation = row[4]
    community_name = row[5]
    price_per_area = row[6]

    print("DATABASE Version: %s, %s, %s, %s, %s, %s, %s" %
          (house_id, house_title, price, total_area, orientation, community_name, price_per_area))

db.close()