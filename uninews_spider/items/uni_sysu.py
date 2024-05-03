import scrapy


class SysuItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
