# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class UninewsSpiderPipeline:
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def open_spider(self, spider):
        host = spider.settings.get('MYSQL_HOST')
        user = spider.settings.get('MYSQL_USER')
        password = spider.settings.get('MYSQL_PASSWORD')
        database = spider.settings.get('MYSQL_DATABASE')
        port = spider.settings.get('MYSQL_PORT')
        self.db_connect = pymysql.connect(host=host, user=user, password=password, database=database, port=port, charset='utf8')
        self.cursor = self.db_connect.cursor()
        print("数据库连接成功")

    def close_spider(self, spider):
        self.db_connect.close()
        print("数据库已关闭")

    def insert_db(self, item):
        values = (
            item['title'],
            item['source'],
            item['date'],
            item['content'],
            item['url'],
            item['crawl_time'],
        )
        sql = 'INSERT INTO test(title, source, date, content, url, crawl_time) VALUES (%s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql,values)
        self.db_connect.commit()
        return item

        # try:
        #     print("准备插入的数据:", values)
        #     self.cursor.execute(sql, values)
        #     self.db_connect.commit()
        #     print("数据保存成功")
        # except Exception as e:
        #     print("数据保存失败:", e)