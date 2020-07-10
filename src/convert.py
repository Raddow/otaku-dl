import img2pdf
import os

# converte todos os arquivos terminados em .jpg dentro de um diretorio ectory
def convert_pdf(dirname, pdf_name):
	with open(pdf_name,"wb") as f:
		imgs = []
		for fname in os.listdir(dirname):
			if not (fname.endswith(".jpg")) or (fname.endswith(".png")):
				continue
			path = os.path.join(dirname, fname)
			if os.path.isdir(path):
				continue
			imgs.append(path)
		f.write(img2pdf.convert(imgs))