import os
import pathlib
from bs4 import BeautifulSoup
from pegahtml import get_html as gtml


def download_manga(manga, capI, capF, linkao):
	#loop range dos capitulos inicio e fim

	def cd(dir):
	    if not os.path.exists(dir):  # check for an existing path
	        os.mkdir(dir)  # make directory if it doesn't exist
	    elif not pathlib.Path(dir).is_dir():  # else check for a clashing filename
	        print("Error: A file already exists with '" + dir + "' filename")
	    os.chdir(dir)

	cd("Downloads")
	cd(manga)

	for cap in range(capI, capF+1):
		if cap < 10:
			capao = str(0)+str(cap)
		else:
			capao = str(cap)

		cd(str(capao))

		print("Baixando o capitulo: "+str(capao)+".....")
		url = linkao+str(capao)
		url = url.replace(' ', '%20')
		html = gtml(url)
		soup = BeautifulSoup(html, "html.parser")

		try:
			for link in soup.find_all('img'):
				if link.get('src')[:38] == 'https://unionleitor.top/leitor/mangas/':
					download_command = "#!/bin/bash \ncurl -O "+str(link.get('src').replace(' ', '%20').replace('(', '\(').replace(')', '\)'))
					print(download_command)
					os.system(download_command)
		except:
			break

		path = os.getcwd()
		print("Your downloaded file is in this path:\n"+path)
		os.chdir("..")