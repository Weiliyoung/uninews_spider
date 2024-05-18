# 广东金融学院

import scrapy
from datetime import datetime
from uninews_spider.items.uni_gduf import GdufItem


class GDUFSpider(scrapy.Spider):
    name = 'gduf_spider'
    allowed_domains = ['yjs.gduf.edu.cn']
    start_urls = ['https://yjs.gduf.edu.cn/']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 下载延迟
        'CONCURRENT_REQUESTS': 16,  # 减少并发请求数
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,  # 针对同一域名的并发请求
    }

    def parse(self, response):
        self.logger.debug("Parsing started for URL: %s", response.url)

        # 在此处添加提取招生就业链接的代码
        recruitment_url = response.xpath('//a[text()="招生工作"]/@href').get()
        if recruitment_url:
            yield response.follow(recruitment_url, callback=self.parse_news_list)

    def parse_news_list(self, response):
        # 提取所有新闻条目的链接
        news_links = response.xpath('//div[@class="main_conRCb"]/ul/li/a/@href').getall()
        self.logger.info(f"当前页面 {response.url} 包含的所有的url: {news_links}")
        for link in news_links:
            yield response.follow(link, callback=self.parse_news_content)

        # 提取下一页的链接并递归跟踪
        next_page_link = response.xpath('//div/table/tbody/tr/td/table/tbody/tr/td[2]/div/span[3]/@href').get()
        if next_page_link:
            self.logger.info(f"下一页的链接：{next_page_link}")
            yield response.follow(next_page_link, callback=self.parse_news_list)
        else:
            self.logger.info(f"没有下一页了")

    def parse_news_content(self, response):

        # 提取标题
        title = response.xpath('//div/form//div/h2/text()').get().strip()

        # 提取时间
        date = response.xpath('//div[@class="main_content"]/div/p/text()').get().strip()

        # 提取内容，合并所有段落
        content = ''.join(response.xpath('//*[@id="vsb_content_502"]/p//text()').getall()).strip()

        # 页面URL
        url = response.url

        # 爬虫时间
        crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        item = GdufItem(
            title=title,
            date=date,
            content=content,
            url=url,
            crawl_time=crawl_time,
        )

        # 组装数据
        yield item  # 返回Item对象
