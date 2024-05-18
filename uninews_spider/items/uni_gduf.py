# 广东金融学院
# 服务于spiders.uni_gduf_spider.py文件
# mysql字段的定义

import scrapy


class GdufItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass