from urllib import parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def search_on_server(server, manga):
    if server == 1:
        #unionleitor
        linkosos = []
        real_links = []
        dicio_links_form = {}

        #parte1: busca

        data = parse.urlencode({"pesquisa":manga}).encode('utf-8')
        req = Request('https://unionleitor.top/busca', data=data, headers={'Host': 'unionleitor.top', 'User-Agent': 'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Origin': 'https://unionleitor.top'})
        webpage = urlopen(req).read()

        soup = BeautifulSoup(webpage, 'html.parser', from_encoding="iso-8859-1")

        for link in soup.findAll("a", string=True):
            linkosos.append(link["href"])

        i = 1
        for linkoso in linkosos:
            if linkoso[:30] == 'https://unionleitor.top/manga/':
                dicio_links_form[i] = [linkoso[30:].replace('-', ' ').title(), linkoso]
                i = i + 1

        for key, value in dicio_links_form.items():
            print("\n["+str(key)+"]"+" "+ "-"+" "+str(value[0]))

        number = int(input(("\nSelecione o numero do manga: ")))
        #number = 13
        manga_link = dicio_links_form[number]

        #parte2: pegue o link

        req = Request(manga_link[1], headers={'Host': 'unionleitor.top', 'User-Agent': 'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Origin': 'https://unionleitor.top'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser', from_encoding="iso-8859-1")
        link = soup.find('a', text='Cap. 01')
        finally_link = str(link["href"])
        finally_link = finally_link.replace('01', '')

        #print(finally_link)
        return finally_link

    else:
    	print('Server Not Found. Sorry =(')