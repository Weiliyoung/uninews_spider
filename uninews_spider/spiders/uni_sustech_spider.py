# 南方科技大学硕士招生公告

import scrapy
import json
from datetime import datetime
from uninews_spider.items.uni_gdut import GdutItem


class SUSTECHpider(scrapy.Spider):
    name = 'sustech_spider'
    allowed_domains = ['yzw.gdut.edu.cn']
    start_urls = ['https://yzw.gdut.edu.cn/']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 下载延迟
        'CONCURRENT_REQUESTS': 16,  # 减少并发请求数
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,  # 针对同一域名的并发请求
    }

    # 硕士招生
    # 爬取硕士招生目录的链接
    def parse(self, response):
        self.logger.debug("Parsing started for URL: %s", response.url)

        # 在此处添加提取硕士招生链接的代码
        recruitment_url = response.xpath('//a[text()="硕士招生"]/@href').get()
        if recruitment_url:
            yield response.follow(recruitment_url, callback=self.parse_recruitment_list)

    # 爬取硕士招生公告
    def parse_recruitment_list(self, response):
        self.logger.debug("Parsing started for URL:%s", response.url)
        # 在此添加提取硕士招生所有公告链接
        news_links = response.xpath('//div[@class="main_conRCb"]/ul/li/a/@href').getall()
        self.logger.info(f"当前页面 {response.url} 包含的所有的url: {news_links}")
        for link in news_links:
            yield response.follow(link, callback=self.parse_news_content)

        # 提取下一页的链接并递归跟踪
        next_page_link = response.xpath('//div//table//td[2]/div/a[1]/@href').get()
        if next_page_link:
            self.logger.info(f"下一页的链接: {next_page_link}")
            yield response.follow(next_page_link, callback=self.parse_news_content)
        else:
            self.logger.info(f"没有下一页")

    # 爬取数据
    def parse_news_content(self, response):
        # 提取标题
        title = response.xpath('//h2/text()').get()
        if title is not None:
            title = title.strip()

        # 提取时间
        date = response.xpath('//div[3]/form/div/div[1]/p/text()').get().strip()

        # 提取内容
        text_content = response.xpath('//*[@id="vsb_content_500"]//div[1]/p/span').getall()
        content = json.dumps(text_content, ensure_ascii=False).strip()

        # 页面URL
        url = response.url

        # 爬虫时间
        crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        item = GdutItem(
            title=title,
            date=date,
            content=content,
            url=url,
            crawl_time=crawl_time,
        )
        yield item  # 返回Item对象
