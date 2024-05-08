# 华南师范大学
# 服务于spiders.uni_scnu.py文件
# mysql字段的定义
import scrapy


class ScnuItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
