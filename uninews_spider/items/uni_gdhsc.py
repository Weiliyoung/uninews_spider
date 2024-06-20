# 广州华商学院
# 服务于spiders.uni_gdhsc.py文件
# mysql字段的定义
import scrapy


class TestItem(scrapy.Item):
    id = scrapy.Field()
    university_name = scrapy.Field()
    city_name = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()
    crawler_task_id = scrapy.Field()
    crawler_name = scrapy.Field()


pass
