from typing import Any
import scrapy
from scrapy.http import Response
from scrapy.selector import Selector
from ..items import CrawlNewspaperItem
import re

from ..db_connector.connector import get_all_websites, get_categories, get_contents
import json

class NewsSpider(scrapy.Spider):
    name = 'news'

    def start_requests(self):
        web_list = get_all_websites()
        
        for website in web_list: 
            domain = website[1] 
            categories = json.loads(website[2])
            
            for cat in categories:
                url = domain + cat
                yield scrapy.Request(url=url, callback=self.parse_link, meta={"website_id": website[0], "domain": domain})

    def parse_link(self, response):
        result = set()
        url_pattern = re.compile(f"^{re.escape(response.meta.get("domain"))}[^\/]*\\.html$")

        x_path_categories = get_categories(response.meta.get("website_id"))
        for cate in x_path_categories:
            x_path = cate + '//a/@href'
            href_list = response.xpath(x_path).getall()

            for href in href_list:
                if (len(href) >= 50 and ('http' not in href)):
                    result.add(response.meta.get("domain") + href)
                elif len(href) >= 50 and url_pattern.match(href):
                    result.add(href)

        for item in result:
            yield scrapy.Request(url=item, callback=self.parse, meta={"website_id": response.meta.get("website_id")})

    def parse(self, response: Response, **kwargs: Any):
        posts = get_contents(response.meta.get("website_id"))

        for post in posts:
            content = response.xpath(post["content"]).get()
            title = response.xpath(post["title"] + "//text()").get()
            date = response.xpath(post["date"] + "//text()").get()

            crawlerItem = CrawlNewspaperItem()
            crawlerItem['content'] = content
            crawlerItem['title'] = title.strip() if title != None else title
            crawlerItem['date'] = date.strip() if date != None else date
            crawlerItem['url'] = response.url

            yield crawlerItem

            