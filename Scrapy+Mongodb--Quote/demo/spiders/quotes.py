import scrapy
from bs4 import BeautifulSoup
from demo.items import QuoteItem
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        quotes = soup.find_all('div',class_='quote')
        
        for quote in quotes:
            item = QuoteItem()
            quoteSoup = BeautifulSoup(str(quote),'lxml')
            item['text'] = quoteSoup.find('span',class_='text').string
            item['author'] = quoteSoup.find('small').string
            item['tags'] = [tag.string for tag in quoteSoup.find_all('a',class_='tag')]
            yield item

        nextPage = soup.find('nav').find_all('a')[-1].get('href')
        nextUrl = response.urljoin(nextPage)
        yield scrapy.Request(url=nextUrl, callback=self.parse)