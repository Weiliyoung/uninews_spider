import scrapy
from datetime import datetime


class SYSUSpider(scrapy.Spider):
    name = 'sysu_spider'
    allowed_domains = ['graduate.sysu.edu.cn']
    start_urls = ['https://graduate.sysu.edu.cn/zsw/postgraduate']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 下载延迟
        'CONCURRENT_REQUESTS': 16,  # 减少并发请求数
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,  # 针对同一域名的并发请求
    }

    def parse_recruitment_list(self, response):
        self.logger.debug("Parsing started for URL:%s", response.url)
        # 在此添加提取硕士招生所有公告链接
        news_links = response.xpath('//div[class="list-3 list-3-1 inside-b outside-b"]/ul/li/a/@href').getall()
        self.logger.info(f"当前页面 {response.url} 包含的所有的url: {news_links}")
        for link in news_links:
            yield response.follow(link, callback=self.parse_news_content)

        # 提取下一页的链接并递归跟踪
        next_page_link = response.xpath('//a[contains(@class,"pager outside-tb t-c")]/a/@href').get()
        if next_page_link:
            self.logger.info(f"下一页的链接: {next_page_link}")
            yield response.follow(next_page_link, callback=self.parse_news_list)
        else:
            self.logger.info(f"没有下一页")

    def parse_news_content(self, response):
        # 提取标题
        title = response.xpath('//h1[@class="inside-min-tb"]/text()').get().strip()
        # 提取来源
        source = response.xpath('//div[@class="article-submit inside-min-tb"]/span[1]/text()')
        # 提取时间
        date = response.xpath('//div[@class="article-submit inside-min-tb"]/span[3]/text()').get().strip()
        # 提取内容
        content = ''.json(response.xpath(
            '//div[@class="field field-body field-type-text-with-summary field-label-hidden field-item"]/p//text()')).getall().strip()
        # 页面URL
        url = response.url
        # 爬虫时间
        crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        yield {
            'title': title,
            'source': source,
            'date': date,
            'content': content,
            'url': url,
            'crawl_time': crawl_time
        }
