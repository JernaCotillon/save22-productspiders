import scrapy
from save22_productspiders.items import SampleItem

class AllForYouu(scrapy.Spider):
    name = "allforyou"
    allowed_domains = ["allforyou.sg"]
    start_urls = [
        "https://allforyou.sg/",
    ]

    def parse(self, response):
        for href in response.css("div.span2.categorybox-span > div.categorybox.thumbnail.text-center > div.thumb > a::attr('href')"):   
          url = response.urljoin(href.extract())
          #print "Category link --> " + url
          request = scrapy.Request(url, callback=self.parse_2)
          yield request


    def parse_2(self, response):
        for href in response.css("div.FeaturedHeader > h2 > a::attr('href')"):
          url = response.urljoin(href.extract())    
          request = scrapy.Request(url, callback=self.parse_dir_contents)
          yield request      

    def parse_dir_contents(self, response):
        items = list()

        for sel in response.xpath('//div[@class="prod-data"]'):
            item = SampleItem()
            item['url'] = response.url or None
            item['title'] = sel.xpath('@data-name').extract()
            item['description'] = sel.xpath('@data-desc').extract()
            item['img_urls'] = sel.xpath('@data-imgurl').extract()
            item['sku'] = sel.xpath('@id').extract()
            item['price'] = sel.xpath('@data-price').extract()
            item['oldprice'] = sel.xpath('@data-oldprice').extract()
            item['outofstock'] = sel.xpath('@data-outofstock').extract()
            item['offer'] = sel.xpath('@data-offername').extract()
            item['categories'] = sel.xpath('//title/text()').extract()[0]
            items.append(item)
            yield item

        next_page = response.css("div.pager > a::attr('href')")
        if next_page:
            nextPages = response.urljoin(next_page[0].extract())
            print "Next Page--> " + nextPages
            yield scrapy.Request(nextPages, self.parse_dir_contents)
        