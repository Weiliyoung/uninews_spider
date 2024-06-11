import scrapy
from datetime import datetime
from uninews_spider.items.uni_gdhsc import TestItem


class GDHSCSpider(scrapy.Spider):
    name = 'gdhsc_spider'
    allowed_domains = ['gdhsc.edu.cn']
    start_urls = ['https://www.gdhsc.edu.cn/']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 下载延迟
        'CONCURRENT_REQUESTS': 16,  # 减少并发请求数
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,  # 针对同一域名的并发请求
    }

    def parse(self, response):
        self.logger.debug("Parsing started for URL: %s", response.url)
        # 在此处添加提取招生就业链接的代码
        recruitment_url = response.xpath('//a[text()="招生就业"]/@href').get()
        if recruitment_url:
            yield response.follow(recruitment_url, callback=self.parse_recruitment_news)
        # yield response.follow('/zsyw.htm', callback=self.parse_news_list)

    def parse_recruitment_news(self, response):
        self.logger.debug("Parsing recruitment news URL: %s", response.url)
        # 在此处添加提取招生要闻数据的代码
        recruitment_news = response.xpath('//a[text()="招生要闻"]/@href').get()
        if recruitment_news:
            yield response.follow(recruitment_news, callback=self.parse_news_list)

    def parse_news_list(self, response):
        # 提取所有新闻条目的链接
        news_links = response.xpath('//div[@class="l_right fr"]/ul/li/a/@href').getall()
        self.logger.info(f"当前页面 {response.url} 包含的所有的url: {news_links}")
        for link in news_links:
            yield response.follow(link, callback=self.parse_news_content)

        # 提取下一页的链接并递归跟踪
        next_page_link = response.xpath('//span[contains(@class, "p_next")]/a/@href').get()
        if next_page_link:
            self.logger.info(f"下一页的链接：{next_page_link}")
            yield response.follow(next_page_link, callback=self.parse_news_list)
        else:
            self.logger.info(f"没有下一页了")

    def parse_news_content(self, response):
        # 提取标题
        title = response.xpath('//h3[@class="l_h3"]/text()').get().strip()
        # 提取来源
        source = response.xpath('//div[@class="l_zy"]/div[@class="fl"]/font[3]/text()').extract_first(
            default='未知').strip()
        # 提取时间
        date = response.xpath('//div[@class="l_zy"]/div[@class="fl"]/font[1]/text()').get().strip()
        # 提取内容，合并所有段落
        content = ''.join(response.xpath('//div[@class="v_news_content"]/p//text()').getall()).strip()
        # 页面URL
        url = response.url
        # 爬虫时间
        crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_id = self.settings.get('CRAWLER_TASK_ID')

        item = TestItem(
            university_name="广州华商学院",
            crawler_task_id=task_id,
            city_name="广州市",
            title=title,
            source=source,
            date=date,
            content=content,
            url=url,
            crawl_time=crawl_time,
        )

        # 组装数据
        yield item  # 返回Item对象
        # yield {
        #     'title': title,
        #     'source': source,
        #     'date': date,
        #     'content': content,
        #     'url': url,
        #     'crawl_time': crawl_time
        # }
