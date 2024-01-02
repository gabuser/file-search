# file-search
o file-search é um buscador de arquivos que foi criado com objetivo de ajudar as pessoas a procurar arquivos perdidos em sua máquina.

> nota: esse é um buscador de arquivos simples, então pode ser que algumas funcionalidades estejam de fora. 

## requisitos

```
$ python instalado
$ ambientes linux(porém possa ser que em windows funcione, mas eu não testei)
``` 

### donwloads
abra seu terminal e digite o seguinte comando: 
> $ git clone https/URL desse repositório 

antes de fazer o git clone, tenha em mente um local de armazenamento que deseja copiar o diretório, por exemplo: 
> $ |inicio|usuario| git clone
###
em seguida:
`` $ python3 main.py``

#### casos de erro
se voce tentar buscar um arquivo que tem privilégios de administrador então pode ser que ocorra um erro, para concertar use em seu terminal: 

``$ sudo python3 main.py``

caso tente encontrar um diretório ao invés do arquivo, então irá retornar como "não encontrado", necessita ser um arquivo.