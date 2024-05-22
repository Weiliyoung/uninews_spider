# 广州体育学院
# 服务于spiders.uni_gzsport.py文件
# mysql字段的定义
import scrapy


class GzsportItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
