import sys
import getopt
from search import search_on_server as sos
from downloadManga import download_manga as dm

#global variables
manga = ''
directory = 'Downloads/'
typoso = ''
server = 1
capI = 0
capF = 0
caps = False
search = False


def usage():
	print('Otaku Downloader Tool')
	print('')
	print('Exemplo de uso: python main.py -mg manga -cI baixe_esse_cap -cF termine_nesse_cap')
	print('-m --manga 						- Pesquisa por um manga no database.')
	print('-ci --capituloInicial			- Baixe esse capitulo')
	print('-ci --capituloFinal				- Terminar de baixar por esse capitulo')
	print('-caps -capitulos					- Baixe todos os capitulos existentes')
	print('-t --type						- Tipo de arquivo dos mangas: pdf ou kindle. Padrao: pasta de imagens')
	print('-d --directory					- Diretorio de onde os mangas devem ficar')
	print('-ls --list						- Liste todos os capitulos disponiveis')
	print('-h --help						- Liste todos os comandos')
	print('')
	print('')
	print('Exemplos: ')
	print('python main.py -m kimetsu no yaiba -caps')
	print('python main.py -m boku no hero -cI 195 -t kindle')
	print('python main.py -m naruto -cI 1 -cF 10 -t pdf -d=/home/Downloads')
	sys.exit(0)


def main():
	global manga
	global directory
	global server
	global capI
	global capF
	global caps
	global search

	if not len(sys.argv[1:]):
		usage()

	# read the commandline options
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
			["manga", "help", "list", "capituloInicial", "capituloFinal", "capitulos", "directory", "type"])
	except getopt.GetoptError as err:
		print(str(err))
		usage()


	for o,a in opts:
		if o in ("-h", "--help"):
			usage()
		elif o in ("-m", "--manga"):
			manga = a
		elif o in ("-ci", "--capituloInicial"):
			capI = a
		elif o in ("-cf", "--capituloFinal"):
			capF = a
		elif o in ("-d", "--directory"):
			directory = a
		elif o in ("-t", "--type"):
			typoso = a
		elif o in ("-caps", "--capitulos"):
			caps = True
		elif o in ("-ls", "--list"):
			search = True
		else:
			assert(False, "Unhandled Option")


if __name__ = "__main__":
	main()
	server = 1
	
	#manga = 'naruto'

	#capI = 1 
	#capF = 1
	
	if not manga == '':
		the_link = sos(server, manga, search)
		dm(the_link[0], capI, capF, caps, the_link[1], typoso, directory)