<h1 align="center">Heeds</h1>

<p align="center">Esse site foi desenvolvido com o 
intuito de ajudar vendedores a visitar varios 
estabelecimentos apenas colocando o nome do local
na barra de pesquisa</p>

<br>
Tabela de conteúdos <br>
===================

*[sobre](#sobre)<br>
*[tecnologias](#tecnologias)

<h4>Django Select &#128640; Em contrução ...</h4>

### Features

- [x] Usuario consegue inserir os locais visitados com o nome
- [x] Usuario consegue listar os locais visitidados, foi feita uma screen justamente para isso
- [x] Usuario consegue editar e deletar o nome do local visitado, a partir da pagina (place) lá o usuário será redirecionado para a pagina "update" caso queeira atualizar o nome do local ou "delete" caso queira deletar o local
- [ ] O Usuario ainda não consegue filtrar os locais visitados por região

### Pré-requisitos
 
Antes de começar, você vai precisar ter 
instalado em sua máquina as seguintes ferramentas
[Git](https://git-scm.com) ou rodar o código "sudo apt install git-all" caso esteja rodando no linux Ubuntu ou em 
alguma distro baseada no Debian e [Django](https://www.djangoproject.com/).
<br>
Além disto é bom ter um editor para trabalhar com 
o código com [VSCode](https://code.visualstudio.com)
ou [Pycharm](https://www.jetbrains.com/pycharm/)

### Rodando o Back End (Servidor local)
```bash
# Clone este repositório
$ git clone <https://github.com/Murilo831/heeds_Murilo.git>

# Acesse a pasta do projeto no terminal/cmd
$ cd heeds_Murilo

# Rode a aplicação
$ source venv/bin/activate #-> inicia o venv
$ deactivate #-> desativa o venv

# Para iniciar o server
$ python manager.py runserver
```

### Tecnologias 
- [Django](https://www.djangoproject.com/)
- [Bootstrap4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

