# 广州医科大学
# 服务于spiders.uni_gzhmu_spider.py文件
# mysql字段的定义

import scrapy


class GzhmuItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass