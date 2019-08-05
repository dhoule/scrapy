#!/usr/bin/env python3
import scrapy


class QuotesSpider(scrapy.Spider):
  # `name` identifies the Spider. It must be unique within a project, 
    # that is, you can't set the same name for different Spiders.
  name = "quotes" 

  # Shortcut for implementing start_requests(), is to use start_urls instead.
    # The parse() method will be called to handle each request of the URLs.
    # This is because parse() is Scrapy's default callback method.
  start_urls = [
    'http://quotes.toscrape.com/page/1/',
  ]
  # method that will be called to handle the response downloaded for 
    # each of the requests made. The response parameter is an instance 
    # of TextResponse that holds the page content and has further 
    # helpful methods to handle it.
    # NOTE: The parse() method usually parses the response, extracting 
      # the scraped data as dicts and also finding new URLs to follow 
      # and creating new requests (Request) from them.
  def parse(self, response):
    for quote in response.css('div.quote'):
      yield {
        'text': quote.css('span.text::text').get(),
        'author': quote.css('span small::text').get(),
        'tags': quote.css('div.tags a.tag::text').getall(),
      }
    
    for a in response.css('li.next a'):
      # response.follow(a) uses the `href` attribute autimatically 
      yield response.follow(a, callback=self.parse)

  
