# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project(scrapy.Item):
    title = scrapy.Field()
    budget = scrapy.Field()
    date = scrapy.Field()
    applicants_number = scrapy.Field()
    description = scrapy.Field()
    skills = scrapy.Field()
    creator = scrapy.Field()
    short_link = scrapy.Field()
    remaining_time = scrapy.Field()
    last_modified = scrapy.Field()
