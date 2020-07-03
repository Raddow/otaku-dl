from search import search_on_server as sos
from downloadManga import download_manga as dm

#print("(1)- Union leitor")
#server = int(input("Digite o numero do server de mangas que voce quer: "))
server = 1

#manga = 'naruto'
manga = input('Digite o manga: ')

print("Digite o inicio e o fim dos capitulos: ")
capI = int(input("Inicio: "))
capF = int(input("Fim: "))
#capI = 1 
#capF = 1

the_link = sos(server, manga)
print(the_link)
dm(the_link[0], capI, capF, the_link[1])