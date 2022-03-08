import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/js']

    script = '''
    function main(splash, args)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        return splash:html()
    end
    '''

    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        for element in response.xpath("//div[@class='quote']"):
            yield {
                "quote": element.xpath(".//span/text()").get(),
                "author": element.xpath(".//span/small[@class='author']/text()").get(),
                "tags": element.xpath(".//div[@class='tags']/a[@class='tag']/text()").extract(),
            }
