import scrapy
class quo(scrapy.Spider):
	name='tln'
	start_urls=['https://www.india.gov.in/topics/travel-tourism/approved-agents']
	
	def parse(self, response):
		links=response.css('h3 a::attr(href)').extract();dd=dict()
		for x in range(len(links)):
			dd[x]=links[x]
		
		yield dd