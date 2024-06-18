# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
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
                                          database=self.database, port=self.port, charset='utf8mb4')
        self.cursor = self.db_connect.cursor()
        print("数据库连接成功")

        # 创建爬虫任务
        url = spider.start_urls[0]
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_sql = """
            INSERT INTO crawler_task (url, crawler_name, status, create_time, update_time)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (url, '爬取任务创建', 0, create_time, create_time))
        self.db_connect.commit()

        self.cursor.execute("SELECT LAST_INSERT_ID()")
        self.task_id = self.cursor.fetchone()[0]
        self.task_name = '爬取成功'

        # 设置爬虫任务 ID 和名称到爬虫实例中
        spider.crawler_task_id = self.task_id
        spider.crawler_name = self.task_name

    def close_spider(self, spider):
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = 0 if self.items_scraped > 0 else 1
        crawler_name = '爬取成功' if self.items_scraped > 0 else '爬取失败'

        sql = "UPDATE crawler_task SET status=%s, update_time=%s, crawler_name=%s WHERE id=%s"
        self.cursor.execute(sql, (status, update_time, crawler_name, self.task_id))
        self.db_connect.commit()

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

    def check_exists(self, item):
        sql = 'SELECT 1 FROM article WHERE url = %s'
        self.cursor.execute(sql, (item['url'],))
        return self.cursor.fetchone()

    def get_university_id(self, item):
        university_name = item.get('university_name')
        if not university_name:
            return None  # 或者抛出一个异常

        self.cursor.execute('SELECT id FROM university WHERE university_name = %s', (university_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            # 如果没有找到，可能需要插入新的university记录
            city_id = self.get_city_id(item)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute(
                'INSERT INTO university (city_id, university_name, create_time, update_time) VALUES (%s, %s, %s, %s)',
                (city_id, university_name, current_time, current_time))
            self.db_connect.commit()
            return self.cursor.lastrowid

    def get_city_id(self, item):
        city_name = item.get('city_name')
        if not city_name:
            return None  # 或者抛出一个异常

        self.cursor.execute('SELECT id FROM city WHERE city_name = %s', (city_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            # 如果没有找到，可能需要插入新的city记录
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute(
                'INSERT INTO city (city_name, create_time, update_time) VALUES (%s, %s, %s)',
                (city_name, current_time, current_time))
            self.db_connect.commit()
            return self.cursor.lastrowid

    def insert_db(self, item):
        university_id = self.get_university_id(item)

        # 动态生成字段和对应的值
        fields = ['university_id', 'crawler_task_id']
        values = [university_id, item['crawler_task_id']]

        if 'title' in item:
            fields.append('title')
            values.append(item['title'])

        if 'source' in item:
            fields.append('source')
            values.append(item['source'])

        if 'date' in item:
            fields.append('date')
            values.append(item['date'])

        if 'content' in item:
            fields.append('content')
            values.append(item['content'])

        if 'url' in item:
            fields.append('url')
            values.append(item['url'])

        if 'picture' in item:
            fields.append('picture')
            values.append(item['picture'])

        if 'attachment_url' in item:
            fields.append('attachment_url')
            values.append(item['attachment_url'])

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields.append('crawl_time')
        values.append(current_time)

        # 动态生成SQL
        fields_str = ', '.join(fields)
        values_placeholder = ', '.join(['%s'] * len(values))
        sql = f'INSERT INTO article ({fields_str}) VALUES ({values_placeholder})'

        self.cursor.execute(sql, values)
        self.db_connect.commit()
        print("数据插入成功")
