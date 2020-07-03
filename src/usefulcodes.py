#convert to pdf

pdf_name = "chap"+chapno+".pdf"
pdf_command = "convert *.jpg ../"+pdf_name
os.system(pdf_command)
print("Cleaning up.....")
path = os.getcwd()
print("Your downloaded file is in this path:\n"+path)
os.chdir("..")
open_command = "gnome-open "+pdf_name
os.system(open_command)
shutil.rmtree(str(chap))

#convert to kindle

#https://github.com/jiaweihli/manga_downloader/tree/master/src/ConvertPackage

'''Funcoes:
Baixar:
*mangas pt-br, nihongo, english
*animes pt-br
*anime de ultima data

Pronto:
1-Peca ao usuario o nome do que ele quer
2-Peca para ele selecionar o servidor
3-Peca para ele colocar o numero do capitulo q ele quer

Funcionamento:
 -Pesquise no Union leitor o manga
 	-Encode a data do websocket para a barra /busca
 	-Traga de volta todos os links da busca
 	-Identifique qual é o mais semelhante de acordo com a pesquisa do usuario
 	-Ou dê a ele uma lista de links (que veio de um dicionario), para ele escolher o manga
 	-Quando ele escolher, vá para o site e depois para o leitor para conseguir o link desejado na URL
 -Ou faça um google hacking search da url do leitor e pegue o primeiro link
 	-inurl:"unionleitor.top/leitor" intitle:"manga"
 -Crie um diretorio para o manga e os capitulos
 -Pergunte ao usuario se ele quer converter os mangas à pdf ou à Kindle file
 -Crie uma estrutura de repetição com esse link para fazer o download de quantos capitulos quiser com o curl
 	-se for pdf n precisa mas se Kindle n sei
 -Informe o progresso do download do curl
 -De OK quando terminar

Preciso:
Saber como acessar um url pelo python, 
arranjar um server otaku bom, 
dicionarios,
google hacking,
lista em dicionarios,
urllib,
beatifulsoup como funciona,
comandos de opcoes,
Curl,
integrar um sistema de repetições nas urls para conseguir o que quer 
e informar o download.


sites mangas pt-br que deixa eu alterar a url:
https://unionleitor.top/aws
https://goldenmangas.online/

'''