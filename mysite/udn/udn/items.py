# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class UdnItem(Item):
    url=Field()
    title=Field()
    post_time=Field()
    content=Field()
    author=Field()
    img_url=Field()
    pre_content=Field()


