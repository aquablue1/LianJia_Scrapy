#coding=utf-8

import MySQLdb
from twisted.enterprise import adbapi
from MySQLdb import cursors

# In order to show chinese correct, set the charset as utf8 is essential.
# charset='utf8'
"""
python27环境下使用
import sys
reload(sys)
sys.setdefaultencoding('utf8')
但在python36下，reload()被取消，无法进行累死操作。
"""

dbparams = dict(
    host= "localhost",
    db= "lianjia_house",
    user="user1",
    passwd="1212",
    charset="utf8",
    # cursorclass=cursors.DictCursor,
    use_unicode=False,
)


dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....


db = MySQLdb.connect(**dbparams)

cursor = db.cursor()

# cursor.execute('SET NAMES gbk')

view_all = "SELECT * FROM nanjing_statistics"

sql = "insert into nanjing_statistics values (003, '又一个好地方啊!', 180, 100, '东南', '天河小区', 18000)"

cursor.execute(sql)

data = cursor.fetchall()

print(data)

for row in data:
    house_id = row[0]
    house_title = row[1]
    price = row[2]
    total_area = row[3]
    orientation = row[4]
    community_name = row[5]
    price_per_area = row[6]

    print("DATABASE Version: %s, %s, %s, %s, %s, %s, %s" %
          (house_id.decode('utf8'), house_title.decode('utf8'), price, total_area, orientation, community_name, price_per_area))

db.close()