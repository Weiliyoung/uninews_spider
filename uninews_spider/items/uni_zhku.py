# 仲恺农业工程学院
# 服务于spiders.uni_zhku.py文件
# mysql字段的定义
import scrapy


class ZhkuItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()


pass
