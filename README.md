# Otaku-Downloader

Um downloader para baixar + de 4.000 mangas em PT-BR

Dedicado ao meu amigo Davidson Francis do Radialle e à todos os Otaku do Brasil.

## Como Usar

Entre na sua linha de comando e dispare:

`python main.py -m "inserir o manga aqui" -I baixe_esse_cap -F finalize_nesse_cap`

O programa te dará uma lista de mangas de acordo com o manga inserido e o usuario deve fornecer o numero para baixar.

O programa irá baixar por padrão, uma pasta de imagens do manga por capítulo.

## Opções

> `-h, --help`

mostra a mensagem de help e sai do programa

> `-m, --manga`

pesquisa o manga na database do unionleitor

> `-I, --capInicial`

Baixa um capitulo

> `-F, --capFinal`

Baixa até esse capitulo

> `-t, --type`

O tipo de arquivo do manga. No momento, só tem pdf. Se o usuário quiser pdf, ele deve dar `-t pdf`. Contudo, essa função se limita a converter apenas as imagens que são .jpg.

> `-c, --caps`

Baixa todos os capítulos existentes

> `-l, --list`

Fornece uma lista de capitulos do manga

> `-d, --directory`

O diretório aonde deve ser baixado os mangas

## Instalações Necessárias
* pip install bs4 tqdm

## New Updates
* Support for Windows, MacOS
* Opções de linha de comando
* Converte para PDF as imagens que são JPG
* Fixed bugs

## Notas

O programa ainda está em fase beta, alguns bugs devem aparecer. Se você presenciou algum problema, por favor, deixe registrado no Issues do github. Irei corrigir o bug quanto antes.

Também, se você quiser contribuir no projeto, deixe-m saber disso =)

Espero que gostem.
