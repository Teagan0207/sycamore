#coding: utf-8 -*-
import scrapy
import time

class MyspiderSpider(scrapy.Spider):
	name = 'myspider'
	def __init__(self,*args,**kwargs):
		self.file = kwargs['filename']
		self.id = 0
	def start_requests(self):
		with open(self.file) as f:
			for line in f:
				url = line.strip()
				yield scrapy.Request(url,callback=self.parse)


	def parse(self,response):
		name   =    response.xpath("//div[@id='title']//h1/text()").extract_first("")
		language =  response.xpath("//li[@class='language']/text()").extract_first("")
		total = response.xpath("//span[@class='track-count']/text()").extract_first("").replace("Items","").replace("Item","").strip()
		start=""
		end=""
		if total != "0":
			start = response.xpath("//td[@class='release-date']//span[@class='text']//text()").extract_first("")
			end =  response.xpath("//td[@class='release-date']//span[@class='text']//text()").extract()[-1]
		with open(self.file+".result.csv","a+",errors="ignore") as f:
			f.write("%d,%s,%s,%s,%s,%s,%s,%s\n" %(self.id,name.replace(","," "),start,end,language,total,response.url,time.strftime("%m/%d/%Y", time.localtime())))
			self.id+=1
