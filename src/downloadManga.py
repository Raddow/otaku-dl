import os
import pathlib
from pegahtml import pega_html as phtml
from downloadFiles import download_url_file as duf

def cd(dir):
	"""
	Um inteligente change directory
	"""
	if not os.path.exists(dir):  # check for an existing path
	    os.mkdir(dir)  # make directory if it doesn't exist
	elif not pathlib.Path(dir).is_dir():  # else check for a clashing filename
	    print("Error: A file already exists with '" + dir + "' filename")
	os.chdir(dir)

def download_manga(manga, capI, capF, linkao):
	#loop range dos capitulos inicio e fim

	cd("Downloads")
	cd(manga)

	for cap in range(capI, capF+1):
		if cap < 10:
			capao = str(0)+str(cap)
		else:
			capao = str(cap)

		cd(str(capao))

		print("Baixando o capitulo: "+str(capao)+".....")

		soup = phtml(linkao+str(capao))
		print(soup)

		for link in soup.find_all('img'):
			if link.get('src')[:38] == 'https://unionleitor.top/leitor/mangas/':
				print(link.get('src'))
				duf(str(link.get('src')))

		path = os.getcwd()
		print("O capitulo do manga "+ str(capao)+ " esta nesse path: :\n"+path)
		os.chdir("..")

"""
download_command = "#!/bin/bash \ncurl -O "+str(link.get('src').replace(' ', '%20').replace('(', '\(').replace(')', '\)'))
					print(download_command)
					os.system(download_command)
"""