from tqdm import tqdm
import requests

def download_url_file(url):
	# leia 1024 bytes toda vez 
	buffer_size = 1024
	# baixe o body do response pelo chunk, e nao imediatamente
	response = requests.get(url, stream=True)
	
	# pegue o total do tamanho do arquivo
	file_size = int(response.headers.get("Content-Length", 0))
	# pegue o nome do arquivo
	filename = url.split("/")[-1]
	
	# barra de progresso, mudando de unidade para bytes ao inves de interacao (padrao tqdm)
	progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
	with open(filename, "wb") as f:
	    for data in progress:
	        # write data read to the file
	        f.write(data)
	        # atualize a barra de progresso manualmente
	        progress.update(len(data))