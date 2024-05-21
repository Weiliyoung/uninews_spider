# 仲恺农业工程学院

import scrapy
from datetime import datetime
from uninews_spider.items.uni_zhku import ZhkuItem


class ZHKUSpider(scrapy.Spider):
    name = 'zhku_spider'
    allowed_domains = ['yjs.zhku.edu.cn']
    start_urls = ['https://yjs.zhku.edu.cn/']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 下载延迟
        'CONCURRENT_REQUESTS': 16,  # 减少并发请求数
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,  # 针对同一域名的并发请求
    }

    def parse(self, response):
        self.logger.debug("Parsing started for URL: %s", response.url)

        # 在此处添加提取招生就业链接的代码
        recruitment_url = response.xpath('//*[@id="a_4_1035"]/a/@href').get()
        if recruitment_url:
            yield response.follow(recruitment_url, callback=self.parse_news_list)
        # yield response.follow('/zsyw.htm', callback=self.parse_news_list)

    def parse_news_list(self, response):
        # 提取所有新闻条目的链接
        news_links = response.xpath('//tbody/tr/td[4]/table[2]/tbody/tr/td/div/ul/li/a/@href').getall()
        self.logger.info(f"当前页面 {response.url} 包含的所有的url: {news_links}")
        for link in news_links:
            yield response.follow(link, callback=self.parse_news_content)

        # 提取下一页的链接并递归跟踪
        next_page_link = response.xpath('//tbody/tr/td[4]/table[2]/tbody/tr/td//div//span[9]/a/@href').get()
        if next_page_link:
            self.logger.info(f"下一页的链接：{next_page_link}")
            yield response.follow(next_page_link, callback=self.parse_news_list)
        else:
            self.logger.info(f"没有下一页了")

    def parse_news_content(self, response):

        # 提取标题
        title = response.xpath('//tbody/tr/td[4]/table[2]/tbody/tr/td/form/table/tbody/tr[1]/td/text()').get().strip()

        # 提取来源
        # source = response.xpath('//div[@class="l_zy"]/div[@class="fl"]/font[3]/text()').extract_first(
        #     default='未知').strip()

        # 提取时间
        # date = response.xpath('//h3/text()').get().strip()

        # 提取内容，合并所有段落
        content = ''.join(response.xpath('//*[@id="vsb_content"]/div/p/span/text()').getall()).strip()

        # 页面URL
        url = response.url

        # 爬虫时间
        crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        item = ZhkuItem(
            title=title,
            content=content,
            url=url,
            crawl_time=crawl_time,
        )

        # 组装数据
        yield item  # 返回Item对象