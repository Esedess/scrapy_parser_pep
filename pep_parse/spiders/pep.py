import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ('peps.python.org',)
    start_urls = ['https://peps.python.org/']  # pytest wants []

    def parse(self, response):
        all_peps = response.css('section[id=numerical-index] tbody tr')
        for pep_row in all_peps:
            pep_link = pep_row.css('td a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css(
            '.page-title::text').get().split('–', maxsplit=1)
        number = number.replace('PEP', '').strip()
        name = name.strip()
        status = response.xpath(
            '//dt[contains(text(), "Status")]/following-sibling::dd/text()'
        ).get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
