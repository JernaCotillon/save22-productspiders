# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SampleItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    img_urls = scrapy.Field()
    sel_qty = scrapy.Field()
    price = scrapy.Field()
    oldprice = scrapy.Field()
    outofstock = scrapy.Field()
class ExpansysItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    retailer_sku_code = scrapy.Field()
    model = scrapy.Field()
    mpn = scrapy.Field()
    sku = scrapy.Field()
    upc = scrapy.Field()
    ean = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    crawl_time = scrapy.Field()
    promo_price = scrapy.Field()
    promo_qty = scrapy.Field()
    promo_data = scrapy.Field()
    promo_expiry = scrapy.Field()
    current_price = scrapy.Field()
    brand = scrapy.Field()
    pass
    


