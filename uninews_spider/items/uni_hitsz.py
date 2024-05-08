# 哈尔滨工业大学（深圳）
# 服务于spiders.uni_scnu.py文件
# mysql字段的定义
import scrapy


class HitszItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
