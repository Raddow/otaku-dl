import os
import pathlib
import shutil

from convert import convert_pdf as cpdf
from pegahtml import pega_html as phtml
from downloadFiles import download_url_file as duf

def cd(dir):
	"""
	Um inteligente change directory
	"""
	if not os.path.exists(dir):  # cheque por um diretorio existente
	    os.mkdir(dir)  # faca um diretorio se nao existe
	elif not pathlib.Path(dir).is_dir():  # ou cheque por um arquivo com o mesmo nome
	    print("Error: A file already exists with '" + dir + "' filename")
	os.chdir(dir)

def download_manga(manga, capI, capF, linkao, typoso='', caps=False, directory='Downloads/'):

	cd(directory)
	cd(manga)

	if caps:
		capI = 0
		capF = 2000

	if capF == 0:
		capF = capI

	print(capI, capF)

	#loop range dos capitulos inicio e fim
	for cap in range(capI, capF+1):
		if cap < 10:
			capao = str(0)+str(cap)
		else:
			capao = str(cap)

		cd(str(capao))

		print("Baixando o capitulo: "+str(capao)+".....")

		soup = phtml(linkao+str(capao))

		for link in soup.find_all('img'):
			if link.get('src')[:38] == 'https://unionleitor.top/leitor/mangas/':
				duf(str(link.get('src')))

		if typoso == 'pdf':
			print("Convertendo para pdf... (Por favor, cheque se as imagens do manga nao sao .png)")
			pdf_name = manga+"_"+capao+".pdf"
			cpdf(os.getcwd(), pdf_name)

			print("Apagando arquivos desnecessarios.....")
			shutil.move(pdf_name, "..")
			os.chdir("..")
			shutil.rmtree(capao)

		else:		
			os.chdir("..")

		path = os.getcwd()
		print("O capitulo do manga "+ str(capao)+ " esta nesse diretorio:\n"+path)