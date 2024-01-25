# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlNewspaperItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
