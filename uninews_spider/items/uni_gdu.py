# 广州大学
# 服务于spiders.uni_gdu_spider.py文件
# mysql字段的定义

import scrapy


class GduItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    # date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass