from pegahtml import get_html as gtml
from search import search_on_server as sos
from downloadManga import download_manga as dm

#print("(1)- Union leitor")
#server = int(input("Digite o numero do server de mangas que voce quer: "))
server = 1

manga = input('Manga que voce quer: ')
#manga = 'naruto'

print("Digite o inicio e o fim dos capitulos: ")
capI = int(input("Inicio: "))
capF = int(input("Fim: "))


the_link = sos(server, manga)

dm(manga, capI, capF, the_link)