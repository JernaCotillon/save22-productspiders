import scrapy
from save22_productspiders.items import SampleItem

class ExpansysItem(scrapy.Spider):
    name = "expan"
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
        print "PUMASOK"
        #items = list()

        # for sel in response.xpath('//ul[@id=breadcrumbs"]'):
        #   print sel
            # item = SampleItem()
            # item['url'] = response.url or None
            # item['title'] = sel.xpath('@data-name').extract()
            # item['description'] = sel.xpath('@data-desc').extract()
            # item['img_urls'] = sel.xpath('@data-imgurl').extract()
            # item['sel_qty'] = sel.xpath('@data-selqty').extract()
            # item['price'] = sel.xpath('@data-price').extract()
            # item['oldprice'] = sel.xpath('@data-oldprice').extract()
            # item['outofstock'] = sel.xpath('@data-outofstock').extract()
            # items.append(item)
            # yield item
        