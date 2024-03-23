# Kit start

## Descrição
Este é um projeto para formar o que conhecemos de boilerplate, para quando houver a necessidade de inicar um novo projeto web, ter um ponto de partida. \
O objetivo aqui é iniciar um software web com o basico de funcionalidades, contemplando testes e observabilidade.

## Pré-requisitos
- Python >= 3.10
- Django >= 5.0.3

## Instalação
1. Clone o repositório para o seu ambiente local:
```bash
git clone https://github.com/ 
```
2. Substitua o nome do arquivo `.env.example` para `.env`:
```bash
mv .env.example .env
```

## Uso
1. Inicie o servidor de desenvolvimento com docker:
```bash
docker compose up -d
```
2. Entre no terminal do container.
```bash
docker compose exec application sh
```
3. Execute as migrações e criação de um super usuário.
```bash
python manage.py migrate
python manage.py createsuperuser
```
2. Acesse o projeto no seu navegador em [http://localhost:8000](http://localhost:8000)

## Funcionalidades
- Cadastro de usuários com e-mail e senha
- Autenticação de usuários
- Gerenciamento de sessões de usuário

## Estrutura do Projeto
```shell
src/
├── setup/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── managers.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
└── manage.py
```
## Autenticação
Autenticação está sendo gerada a partir da manipulação do modelo de usuário. \
Rotas para autenticação podem serem encontradas em `users.urls`



## Autor
Lucas Silva - [LinkedIn](https://www.linkedin.com/in/lucas-gabriel-vieira-silva/)
