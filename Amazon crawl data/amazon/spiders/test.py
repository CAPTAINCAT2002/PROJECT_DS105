import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['kenh14.vn']
    start_urls = ['http://kenh14.vn/']

    def parse(self, response):
        for i in range(3):
            if i==1:
                yield {'a': 1, 'b': 2, 'c':3}
            if i==2:
                yield {'d': 4, 'b': 2, 'c':3}
