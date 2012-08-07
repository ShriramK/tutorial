#from overview of scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from tutorial.items import TorrentItem

class DmozSpider(CrawlSpider):
	name = 'mininova.org'
	allowed_domains = ['mininova.org']
	start_urls = ['http://www.mininova.org/today']
	rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]
	
	def parse_torrent(self, response):
		x = HtmlXPathSelector(response)
		
		torrent = TorrentItem()
		torrent['url'] = response.url
		torrent['name'] = x.select("//h1/text()").extract()
		torrent['description'] = x.select("//div[@id='descriptin']").extract()
		torrent['size'] = x.select("//div[@id='info-left']/p[2]/text()[2]").extract()
		return torrent

#from original example of scrapy
'''
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class DmozSpider(BaseSpider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
	   "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
	   "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response):
		from scrapy.shell import inspect_response
		inspect_response(response)
		filename = response.url.split("/")[-2]
		open(filename, 'wb').write(response.body)
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//ul/li')
		items = []
		for site in sites:
		   item = DmozItem()
		   item['title'] = site.select('a/text()').extract()
		   item['link'] = site.select('a/@href').extract()
		   item['desc'] = site.select('text()').extract()
		   items.append(item)
		return items
'''