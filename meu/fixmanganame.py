def fix_manga_name(manga):
	"""Deixa o nome do maga legivel para url"""
	manga = manga.title()
	manga = manga.replace(' ', '_')
	return manga