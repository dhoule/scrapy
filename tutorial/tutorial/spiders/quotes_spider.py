#!/usr/bin/env python3
import scrapy


class QuotesSpider(scrapy.Spider):
  # `name` identifies the Spider. It must be unique within a project, 
    # that is, you can't set the same name for different Spiders.
  name = "quotes" 

  # must return an iterable of Requests (you can return a list of 
    # requests or write a generator function) which the Spider will 
    # begin to crawl from. Subsequent requests will be generated 
    # successively from these initial requests.
  # def start_requests(self):
  #   urls = [
  #     'http://quotes.toscrape.com/page/1/',
  #     'http://quotes.toscrape.com/page/2/',
  #   ]
  #   for url in urls:
  #     yield scrapy.Request(url=url, callback=self.parse)

  # Shortcut for implementing start_requests(), is to use start_urls instead.
    # The parse() method will be called to handle each request of the URLs.
    # This is because parse() is Scrapy's default callback method.
  start_urls = [
      'http://quotes.toscrape.com/page/1/',
      'http://quotes.toscrape.com/page/2/',
    ]
  # method that will be called to handle the response downloaded for 
    # each of the requests made. The response parameter is an instance 
    # of TextResponse that holds the page content and has further 
    # helpful methods to handle it.
    # NOTE: The parse() method usually parses the response, extracting 
      # the scraped data as dicts and also finding new URLs to follow 
      # and creating new requests (Request) from them.
  def parse(self, response):
    page = response.url.split("/")[-2]
    filename = 'quotes-%s.html' % page
    with open(filename, 'wb') as f:
      f.write(response.body)
    self.log('Saved file %s' % filename)

  
