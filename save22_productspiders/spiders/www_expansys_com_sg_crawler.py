from datetime import datetime
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from save22_productspiders.items import ExpansysItem


class WwwExpansysComSgCrawler(CrawlSpider):
  name = 'www_expansys_com_sg_crawler'
  allowed_domains = ['expansys.com.sg']
  start_urls = [
      'http://www.expansys.com.sg/'
      ]
  
  rules = [
    Rule(LxmlLinkExtractor(allow=(r'.+/\S+\d+/',),deny = (r'.+/.filter',)),
        callback = 'parse_item',
        follow=True,)
]
  def parse_item(self,response):
            items = list()
            
            for sel in response.xpath('//div[@id="product"]'):
                item = ExpansysItem()
                item['url'] = response.url or None
                item['sku'] = sel.xpath('//div[@id="prod_core"]/ul/li[1]/span/text()').extract()
                item['title'] = sel.xpath('//div[@id="title"]/h1/text()').extract()
                item['description'] = sel.xpath('//div[@id="description"]/h2/text()').extract()
                item['price'] = sel.xpath('//div[@id="prod_core"]/span/ul[@class="details"]/li[@class="price"]/p[@id="price"]/strong/span/text()').extract()
                item['ean'] = sel.xpath('//div[@id="prod_core"]/ul/li[2]/span/text()').extract()
                item['mpn'] = sel.xpath('//div[@id="prod_core"]/ul/li[3]/span/text()').extract()
                item['brand'] = sel.xpath('//div[@id="prod_core"]/ul/li[4]/a/text()').extract()
                item['currency'] = sel.xpath('//p[@id="price"]/meta/@content').extract()
                item['img_urls'] = sel.xpath('//div[@id="prod_left"]/div[2]/a/img/@src').extract()
                item['categories'] = sel.xpath('//li[@id="n_audio"]/div/div[1]/ul/li/a/text()').extract()
                item['availability'] = sel.xpath('//li[@id="stock"]/text()').extract()
                item['rating'] = sel.xpath('//div[@id="review_avg"]/span[1]/text()').extract()
                items.append(item)
                yield item
