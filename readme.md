├── first_proj # Pasta do projeto de Django
│ ├── asgi.py # Modulo que executa o ASGI (Async Server Gateway Interfaz)do projeto 
│ ├── __init__.py # modulo que indica que as pasta é um pacote.
│ ├── settings.py # Modulo onde se espeficia as configurações do django.
│ ├── urls.py #  # modulo onde se configurão as URL do Django
│ └── wsgi.py # Modulo que executa o WSGI (Web Server Gateway Interface) do projeto.
├── manage.py # Arquivo cental de Django para interagir com o projeto.
├── Procfile # Arquivo de configuração do HEROKU para definir os processos a executar.
├── README.md # documentação escrita em markdown do projeto.
├── requirements.txt  # o arquivo que esta listando as librerias que o projeto precisa para funcionar.

1. crio a pasta do repositorio mkdir <nome_pasta>
1.1 ingressa na pasta cd <nome_pasta>
2. criou o entorno virtual python3 -m venv venv
3. configurou o git na pasta git init
3.1 criação do arquivo .gitignore, cmd: touch .gitignore
4. [somente aplica se criou o entorno virtual com venv] Inclui a pasta venv dentro do arquivo .gitignore
5. activei o entorno virtual:
    cmd # for VScode
    venv\Scripts\activate.bat 
6. instalei a versao LTS 3.2.0 do django pip install django==3.2.0
7. Criei o projeto de django django-admin startproject first_proj
8. Troquei o nome da pasta first_proj para src, cmd: mv first_proj src
9. Migrei o conteudo de src para fora dela, cmd: mv src/* .
10. apaguei a pasta src, cmd: rm -r src
11. Criamos um commit dos arquivos do repositorio
11.1 agregamos os arquivos ao stage git add .
11.2 criamos o commit git commit -m "<mensagem>"
12. Criamos um repositorio no github.
12.1 configuramos esse repositorio no repositorio local, cmd: git remote add origin <link_do_repo>
12.2 trocamos o nome do branch local para main, git branch -M main
12.3 subimos as mudancas no repositorio remoto: git push origin main
13. enviamos o link para o professor. (edited) 