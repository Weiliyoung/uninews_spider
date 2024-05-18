# 广东技术师范大学
# 服务于spiders.uni_gduf_spider.py文件
# mysql字段的定义

import scrapy


class GpnuItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass