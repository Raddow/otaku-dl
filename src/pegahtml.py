from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import Request, urlopen

def pega_html(url, post='', data={}):
    """
    Retorna um soup object de um dado url
    """

    data = parse.urlencode(data).encode('utf-8')
    req = Request(url+post, data=data, headers={'User-Agent': 'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser', from_encoding="iso-8859-1")
    
    return soup  # Converts the response into text and return it