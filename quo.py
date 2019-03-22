import scrapy

"""
	for using the out command the spider must have items initialized
	
	this spider wont give any output in the -o output file
"""


class quo(scrapy.Spider):
	name='quo'
	start_urls=['http://quotes.toscrape.com/']
	
	def parse(self, response):
		qu=response.css('.text::text').extract()
		au=response.css('.author::text').extract()
		ww= list(zip(au,qu))
		ww=[" : ".join(O) for O in ww]
		ww='\n'.join(ww)
		
		with open("C:\\Users\\ANIMESH\\Desktop\\scrapy\\tlncr\\tlncr\\spiders\\data.txt","w") as f:
			f.write(str(ww))
		#yield ww