import requests
from lxml.html import fromstring


class ProxyGenerator:
    def get() -> list[str]:
        response = requests.get('https://sslproxies.org/')
        parser = fromstring(response.text)
        return [":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]]) for i in parser.xpath('//tbody/tr')[:100] \
            if i.xpath('.//td[7][contains(text(),"yes")]')]