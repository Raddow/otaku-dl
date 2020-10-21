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
the_link = []


#--help
def usage():
	print('Otaku Downloader Tool')
	print('')
	print('Usagem: python main.py -m manga -I baixe_esse_cap -F finalize_nesse_cap\n')
	print('-m --manga 				- Pesquisa por um manga no database. Strings com espaços devem estar entre aspas')
	print('-I --capInicial				- Baixe esse capitulo')
	print('-F --capFinal				- Terminar de baixar por esse capitulo')
	print('-c --caps				- Baixe todos os capitulos existentes')
	print('-t --type				- Converte as imagens para um arquivo. Apenas PDF')
	print('-d --directory				- Diretorio de onde os mangas devem ficar')
	print('-l --list				- Liste todos os capitulos disponiveis')
	print('-h --help				- Liste todos os comandos')
	print('')
	print('')
	print('Exemplos: ')
	print('python main.py -m "kimetsu no yaiba" -c')
	print('python main.py -m "boku no hero" -I 195 -t pdf')
	print('python main.py -m naruto -I 1 -F 10 -d /home/Downloads/')
	sys.exit(0)


if __name__ == "__main__":

	if not len(sys.argv[1:]):
		usage()

	# read the commandline options
	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:h:ls:I:F:c:d:t:",
			["manga=", "help", "list", "capInicial=", "capFinal=", "caps", "directory=", "type="])
	except getopt.GetoptError as err:
		print(str(err))
		usage()


	for o,a in opts:
		if o in ("-h", "--help"):
			usage()
		elif o in ("-m", "--manga"):
			manga = a
		elif o in ("-I", "--capInicial"):
			capI = int(a)
		elif o in ("-F", "--capFinal"):
			capF = int(a)
		elif o in ("-d", "--directory"):
			directory = a
		elif o in ("-t", "--type"):
			typoso = a
		elif o in ("-c", "--caps"):
			caps = True
		elif o in ("-l", "--list"):
			search = True
		else:
			assert(False, "Unhandled Option")

	server = 1
	#search the mangas
	the_link = sos(server, manga, search)
	#then download them if search is false
	if not search:
		dm(the_link[0], capI, capF, the_link[1], typoso, caps, directory)
