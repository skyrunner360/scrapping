import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
