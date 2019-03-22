import scrapy

"""
	for using the out command the spider must have items initialized
	
	this spider will give output in the -o op file as items has been initialized
"""

from ..items import TlncrItem

from scrapy.http import FormRequest

class quo(scrapy.Spider):
	name='qII'
	start_urls=["http://quotes.toscrape.com/login"]
	
	def parse(self, response):
		csrf=response.css('form input::attr(value)').get()
		
		return FormRequest.from_response(response, formdata={'csrf_token':csrf,'username':'alias','password':'alias'}, callback=self.scrprr)
		
	def scrprr(self, response):
		qu=response.css('.text::text').extract()
		au=response.css('.author::text').extract()
		
		op=TlncrItem()
		op['au']=au
		op['qu']=qu
		
		yield op
		
		
		
		
		