import scrapy


class CryptBBSpider(scrapy.Spider):
    name = 'cryptbb'
    allowed_domains = ['cryptbb2gezhohku.onion']
    start_urls = ['http://cryptbb2gezhohku.onion']

    def parse(self, response):
        if response.url == self.start_urls[0]:
            yield {'url': response.url}
        if not response.xpath("//table//strong/a").get():
            yield {'url': response.url}

        for discovered_url in response.xpath('//a/@href').extract():
            yield response.follow(discovered_url, self.parse)
