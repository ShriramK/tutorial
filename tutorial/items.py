'''
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DmozItem(Item):
    # define the fields for your item here like:
    # name = Field()
	title = Field()
	link = Field()
	desc = Field()
'''
#http://doc.scrapy.org/en/latest/intro/overview.html
from scrapy.item import Item, Field

class TorrentItem(Item):
	url = Field()
	name = Field()
	description = Field()
	size = Field()