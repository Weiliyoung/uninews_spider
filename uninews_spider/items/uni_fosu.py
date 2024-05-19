# 佛山科学技术学院
# 服务于spiders.uni_fosu.py文件
# mysql字段的定义
import scrapy


class FosuItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
