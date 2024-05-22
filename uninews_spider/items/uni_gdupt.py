# 广东石油化工学院
# 服务于spiders.uni_zqu.py文件
# mysql字段的定义
import scrapy


class GduptItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
