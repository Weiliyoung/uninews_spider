# 深圳大学
import scrapy


class SzuItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    # date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
