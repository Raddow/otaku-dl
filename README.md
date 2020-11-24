# otaku-dl

Um downloader para baixar + de 4.000 mangas (PT-BR)

Dedicado ao meu amigo Davidson Francis do Radialle e à todos os Otaku do Brasil.

## Instalações Necessárias
`pip install bs4 tqdm img2pdf`

ou utilize o requirements.txt:
`pip install -r requirements.txt`

## Como Usar

Entre na sua linha de comando e dispare:

`python main.py -m "inserir o manga aqui" -I baixe_esse_cap -F finalize_nesse_cap`

O programa te dará uma lista de mangas de acordo com o manga inserido e o usuario deve fornecer o numero para baixar.

O programa irá baixar por padrão, uma pasta de imagens do manga por capítulo.

## Opções

> `-h, --help`

mostra a mensagem de help e sai do programa

> `-m, --manga`

pesquisa o manga na database do unionleitor. Note que se você digitar uma string com espaços, você deve colocar entre espaços. Exemplo: -m "Nanatsu no taizai"

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


## New Updates `21/10/2020`
* Mudanças feitas nas linhas do código para fazer o programa funcionar;
* Mais comentarios nas linhas do código para ficar mais compreensível;
* Changelog.txt; 
* Licença do projeto.

## Notas

O programa ainda está em fase beta, alguns bugs devem aparecer. Se você presenciou algum problema, por favor, deixe registrado no Issues do github. Irei corrigir o bug quanto antes.

Se você quiser contribuir no projeto, deixe-me saber disso =)

Espero que gostem.
