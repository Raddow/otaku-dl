from search import search_on_server as sos
from downloadManga import download_manga as dm

server = 1

#manga = 'naruto'
manga = input('Digite o manga: ')

print("Digite o inicio e o fim dos capitulos: ")
capI = int(input("Inicio: "))
capF = int(input("Fim: "))
#capI = 1 
#capF = 1

the_link = sos(server, manga)
dm(the_link[0], capI, capF, the_link[1])