# 华南农业大学硕士招生公告

import scrapy
import json
from datetime import datetime
from uninews_spider.items.uni_scau import ScauItem


class SCAUSpider(scrapy.Spider):
    name = 'scau_spider'
    allowed_domains = ['yzb.scau.edu.cn']
    start_urls = ['https://yzb.scau.edu.cn/']
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
        recruitment_url = response.xpath('//table[3]//table[2]//td[2]/table[1]/tbody/tr/td/a/@href').get()
        if recruitment_url:
            yield response.follow(recruitment_url, callback=self.parse_recruitment_list)

    # 爬取硕士招生公告
    def parse_recruitment_list(self, response):
        self.logger.debug("Parsing started for URL:%s", response.url)
        # 在此添加提取硕士招生所有公告链接
        news_links = response.xpath('//*[@id="wp_news_w25"]//td[3]/a/@href').getall()
        self.logger.info(f"当前页面 {response.url} 包含的所有的url: {news_links}")
        for link in news_links:
            yield response.follow(link, callback=self.parse_news_content)

        # 提取下一页的链接并递归跟踪
        next_page_link = response.xpath('//*[@id="wp_paging_w25"]//li[2]/a[3]/@href').get()
        if next_page_link:
            self.logger.info(f"下一页的链接: {next_page_link}")
            yield response.follow(next_page_link, callback=self.parse_news_content)
        else:
            self.logger.info(f"没有下一页")

    # 爬取数据
    def parse_news_content(self, response):
        # 提取标题
        title = response.xpath('//table[3]//tr[2]/td[2]/b/font/text()').get()
        if title is not None:
            title = title.strip()

        # 来源
        source = response.xpath('//table[3]//table//tr[4]//td[3]/text()').get.strip()

        # 提取时间
        date = response.xpath('//table[3]//table//tr[4]//td[5]/text()').get().strip()

        # 提取内容
        text_content = response.xpath('//table//tr//p/span/text()').getall()
        content = json.dumps(text_content, ensure_ascii=False).strip()

        # 页面URL
        url = response.url

        # 爬虫时间
        crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        item = ScauItem(
            title=title,
            source=source,
            date=date,
            content=content,
            url=url,
            crawl_time=crawl_time,
        )
        yield item  # 返回Item对象
