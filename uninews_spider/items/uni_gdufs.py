# 广东外语外贸大学
# 服务于spiders.uni_gdufs_spider.py文件
# mysql字段的定义

import scrapy


class GdufsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass