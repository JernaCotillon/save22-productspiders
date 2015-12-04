import scrapy
from save22_productspiders.items import ExpansysItem
from scrapy.spider import BaseSpider

class Expansys(scrapy.Spider):
    name = "expans"
    allowed_domains = ["expansys.com.sg"]
    start_urls = [
        "http://www.expansys.com.sg/mobile-phones/",
    ]

    def parse(self, response):
        for href in response.css("div#nav > ul.asia.me > li > a::attr('href')"):   
          url = response.urljoin(href.extract())
          print "Category link --> " + url
          request = scrapy.Request(url, callback=self.parse_2)
          yield request


    def parse_2(self, response):
        for href in response.css("div#product_listing > div.productGrid > ul.item.c0 > li.image > a::attr('href')"):
          url = response.urljoin(href.extract())
          print "Items ---> " + url
          request = scrapy.Request(url, callback=self.parse_dir_contents)
          yield request      

    def parse_dir_contents(self, response):
        items = list()
        
        for sel in response.xpath('//ul[@id="breadcrumbs"]'):
            item = ExpansysItem()
            item['url'] = response.url or None
            item['title'] = sel.xpath('//div[@id="title"]/h1/text()').extract()
            item['description'] = sel.xpath('//div[@id="description"]/h2/text()').extract()
            item['price'] = sel.xpath('//div[@id="prod_core"]/span/ul[@class="details"]/li[@class="price"]/p[@id="price"]/strong/span/text()').extract()
            item['sku'] = sel.xpath('//div[@id="prod_core"]/ul/li[1]/span/text()').extract()
            item['ean'] = sel.xpath('//div[@id="prod_core"]/ul/li[2]/span/text()').extract()
            item['mpn'] = sel.xpath('//div[@id="prod_core"]/ul/li[3]/span/text()').extract()
            item['brand'] = sel.xpath('//div[@id="prod_core"]/ul/li[4]/a/text()').extract()
            item['currency'] = sel.xpath('//p[@id="price"]/meta/@content').extract()
            item['img_urls'] = sel.xpath('//div[@id="prod_left"]/div[2]/a/img/@src').extract()
            # item['price'] = sel.xpath('@data-price').extract()
            # item['oldprice'] = sel.xpath('@data-oldprice').extract()
            # item['outofstock'] = sel.xpath('@data-outofstock').extract()
            items.append(item)
            yield item

