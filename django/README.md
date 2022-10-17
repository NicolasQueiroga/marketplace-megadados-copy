# Versão em Django

## Instruções para ativar a API localmente

1. Clone o repositório com um dos comandos abaixo:
  - ```git clone git@github.com:NicolasQueiroga/marketplace-megadados.git```
  - ```git clone https://github.com/NicolasQueiroga/marketplace-megadados.git```
  

2. Navegue até a pasta **fastapi** pelo terminal
  - ```cd marketplace-megadados/django```
  
 
3. Inicie o docker-desktop entrando em seu aplicativo e insira os seguintes comandos:
  - ```docker-compose build```
  - ```docker-compose run api python manage.py makemigrations```
  - ```docker-compose run api python manage.py migrate```
  - ```docker-compose run api python manage.py createsuperuser --email admin@admin.com --username admin --password admin  --skip-checks```
  - ```docker-compose up```
  
  
4. E, por último, acesse a url ```http://localhost:8000/admin```, e faça o login com as seguintes credênciais para ter acesso ao site de administrador:
  - e-mail: ***admin@admin.com***
  - password: ***admin***
