# 深圳大学
# 服务于spiders.uni_szu.py文件
# mysql字段的定义
import scrapy


class SzuItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    # date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
