import datetime import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from save22_productspiders.items import Save22ProductspidersItem

class WwwExpansysComSgCrawler(CrawlSpider):
  name = 'www.expansys_com_sg_crawler'
  allowed_domains ('expansys_com.sg')
  start_urls= [
    'http://www.www.expansys_com.sg/mobile-phones'
  ]
  
  rules = (
    Rule(LinkExtractor(
      allow = (r'(+)',),
      callback = parse_item,
      )),
  )
  
  def parse_item(self,response):
    pass