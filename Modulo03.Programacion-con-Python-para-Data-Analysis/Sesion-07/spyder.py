# para ejecutar: scrapy runspider spyder.py -o citas.csv (se puede cambiar el formato cambiando la extensión)
import scrapy


class citasSpyder(scrapy.Spider):
    name = 'citas'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        for cita in response.css('div.quote'):
            yield {
                'texto': cita.css('span.text::text').get(),
                'autor': cita.xpath('span/small/text()').get()
            }

        pagsig = response.css("li.next a::attr('href')").get()
        if pagsig is not None: # hay página siguiente?
            yield  response.follow(pagsig, self.parse)

