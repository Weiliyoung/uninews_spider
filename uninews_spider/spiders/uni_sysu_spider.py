import scrapy
from datetime import datetime
from uninews_spider.items.uni_sysu import SysuItem


class SYSUSpider(scrapy.Spider):
    name = 'sysu_spider'
    allowed_domains = ['graduate.sysu.edu.cn']
    start_urls = ['https://graduate.sysu.edu.cn/zsw/postgraduate']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 下载延迟
        'CONCURRENT_REQUESTS': 16,  # 减少并发请求数
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,  # 针对同一域名的并发请求
    }

    # def parse(self, response):
    #     self.logger.debug("Parsing started for URL: %s", response.url)
    #
    #     # 在此处添加提取硕士招生链接的代码
    #     recruitment_url = response.xpath('//a[text()="硕士招生"]/@href').get()
    #     if recruitment_url:
    #         yield response.follow(recruitment_url, callback=self.parse_recruitment_news)

    def parse_recruitment_list(self, response):
        self.logger.debug("Parsing started for URL:%s", response.url)
        # 在此添加提取硕士招生所有公告链接
        news_links = response.xpath('//div[@class="views-element-container"]//ul/li/a/@href').getall()
        self.logger.info(f"当前页面 {response.url} 包含的所有的url: {news_links}")
        for link in news_links:
            yield response.follow(link, callback=self.parse_news_content)

        # 提取下一页的链接并递归跟踪
        next_page_link = response.xpath('//div[@class="pager outside-tb t-c"]/ul/li/a/@href').get()
        if next_page_link:
            self.logger.info(f"下一页的链接: {next_page_link}")
            yield response.follow(next_page_link, callback=self.parse_news_list)
        else:
            self.logger.info(f"没有下一页")

    def parse_news_content(self, response):
        # 提取标题
        title = response.xpath('//div[@id="content"]//h1/text()').get().strip()
        # 提取来源
        source = response.xpath(
            '//div[contains(@class, "article-submit inside-min-tb")]/span[1]/text()')
        # 提取时间
        date = response.xpath(
            '//div[contains(@class, "article-submit inside-min-tb")]/span[3]/text()').get().strip()
        # 提取内容
        content = ''.json(
            response.xpath('//div[contains(@class, "field")]/p/span//text()')).getall().strip()
        # 页面URL
        url = response.url
        # 爬虫时间
        crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        item = SysuItem(
            title=title,
            source=source,
            date=date,
            content=content,
            url=url,
            crawl_time=crawl_time,
        )
        yield item  # 返回Item对象
