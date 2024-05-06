# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


from itemadapter import ItemAdapter
import pymysql
from datetime import datetime


class UninewsSpiderPipeline:
    def __init__(self):
        self.items_scraped = 0
        self.items_skipped = 0
        self.items_failed = 0
        self.file_scraped = open('scraped_urls.txt', 'w')  # 用于记录已经成功爬取并存入数据库的 URL
        self.file_skipped = open('skipped_urls.txt', 'w')  # 用于记录跳过不进行处理的 URL
        self.file_failed = open('failed_urls.txt', 'w')  # 用于记录爬取过程中发生错误的 URL

    def open_spider(self, spider):
        self.host = spider.settings.get('MYSQL_HOST')
        self.user = spider.settings.get('MYSQL_USER')
        self.password = spider.settings.get('MYSQL_PASSWORD')
        self.database = spider.settings.get('MYSQL_DATABASE')
        self.port = spider.settings.get('MYSQL_PORT')
        self.db_connect = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                          database=self.database, port=self.port, charset='utf8')
        self.cursor = self.db_connect.cursor()
        print("数据库连接成功")

    def close_spider(self, spider):
        self.db_connect.close()
        self.file_scraped.close()
        self.file_skipped.close()
        self.file_failed.close()
        print(f"数据库已关闭\n总计抓取: {self.items_scraped} 新增, {self.items_skipped} 跳过, {self.items_failed} 失败.")

    def process_item(self, item, spider):
        try:
            if self.check_exists(item):
                self.items_skipped += 1
                self.file_skipped.write(item['url'] + '\n')
                print("数据已存在，无需插入")
                return item
            else:
                self.insert_db(item)
                self.items_scraped += 1
                self.file_scraped.write(item['url'] + '\n')
                return item
        except Exception as e:
            self.items_failed += 1
            self.file_failed.write(item['url'] + '\n')
            spider.logger.error(f"处理 {item['url']} 时出错: {str(e)}")
            return item

    def is_valid_item(self, item):
        required_fields = ['title', 'content', 'url', 'crawl_time']
        for field in required_fields:
            if item.get(field) is None:
                return False
        return True

    def check_exists(self, item):
        sql = 'SELECT 1 FROM test WHERE url = %s'
        self.cursor.execute(sql, (item['url'],))
        return self.cursor.fetchone() is not None

    def insert_db(self, item):
        values = (
            item['title'],
            # item['source'],
            # item['date'],
            item['content'],
            item['url'],
            item['crawl_time']
        )
        sql = 'INSERT INTO test(title, content, url, crawl_time) VALUES (%s, %s, %s, %s)'
        self.cursor.execute(sql, values)
        self.db_connect.commit()
        print("数据插入成功")
