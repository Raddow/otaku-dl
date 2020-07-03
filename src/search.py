from pegahtml import pega_html as phtml

def search_on_server(server, manga):
    if server == 1:
        #unionleitor
        linkosos = []
        real_links = []
        dicio_links_form = {}

        #parte1: busca

        soup = phtml('https://unionleitor.top', '/busca', {"pesquisa":manga})

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
        soup = phtml(manga_link[1])

        link = soup.find('a', text='Cap. 01')
        finally_link = str(link["href"])
        manga_link[1] = finally_link.replace('01', '')
        if link == None: 
            link = soup.find('a', tex='Cap. 00')
            finally_link = str(link["href"])
            manga_link[1] = finally_link.replace('00', '')

        return manga_link

    else:
    	print('Server Not Found. Sorry =(')