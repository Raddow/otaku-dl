# otaku-dl

A python script to download more than 4,000 manga (PT-BR)

Dedicated to my friend Davidson Francis and to all Otaku in the world.

## Necessary Installations
`pip install bs4 tqdm img2pdf`

or use requirements.txt:
`pip install -r requirements.txt`

## How to use

Enter your command line and shoot:

`python main.py -m" insert the manga name here "-I download_this_cap -F finalize_this_cap`

The program will give you a list of manga according to the manga entered and the user must provide the number to download.

The program will download, by default, one folder of manga images per chapter.

## Options

> `-h, --help`

shows the help message and exits the program

> `-m, --manga`

search for manga in the unionleitor database. Note that if you type a string with spaces, you must enclose it between spaces. Example: -m "Nanatsu no taizai"

> `-I, --capInicial`

Download a chapter

> `-F, --capFinal`

Download to this chapter

> `-t, --type`

The file type of the manga. At the moment, you only have pdf. If the user wants pdf, he must give `-t pdf`. However, this function is limited to converting only images that are .jpg.

> `-c, --caps`

Download all existing chapters

> `-l, --list`

Provides a list of manga chapters

> `-d, --directory`

The directory where the sleeves should be downloaded


## Coming Soon
This is what I am planning to do:
> English and Japanese Mangas
> Animes and Movies
