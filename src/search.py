from pegahtml import pega_html as phtml

def search_on_server(server, manga, search=False):
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
        manga_link = dicio_links_form[number]

        #print(manga_link)

        #parte2: transfira o link da lista manga_link para soup
        soup = phtml(manga_link[1])
        #print(soup)
        #here for search all with the argument "-l"
        if search:
            for cap in range(0, 2000):
                if cap < 10:
                    capao = str(0)+str(cap)
                else:
                    capao = str(cap)
                link = soup.find('a', text='Cap. '+capao)
                if (link == None) and (capao == '00'):
                    continue
                elif (link == None) and (capao != '00'):
                    break
                print('Cap. '+capao)
        else:
            link = soup.find('a', text='Cap. 01')
            if not link == None:
                finally_link = str(link["href"]).replace('01', '')
            else: 
                link = soup.find('a', text='Cap. 00')
                finally_link = str(link["href"]).replace('00', '')

            manga_link[1] = finally_link
            #print(manga_link)
            return manga_link

    else:
    	print('Server Not Found. Sorry =(')


'''link = soup.find('a', text='Cap. 00') if link == None: link = soup.find('a', text='Cap. 01')
            finally_link = str(link["href"])
            manga_link[1] = finally_link.replace('00', '')'''
