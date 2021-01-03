# crud-cliente

Repositório criado para uma aplicação com o framework Django que realiza o CRUD (Create, Read, Update, Delete) de clientes. Na realização dos testes do projeto foi usado o VENV. Obs: faltando apenas a realização do teste da views da aplicação app. 

<h2> 💻 Configuração necessária para rodar o projeto</h2>

1. Após clonar o repositório em seu computador, mova-se para dentro da pasta do projeto e realize a criação de ambiente virtual para rodar a aplicação:
```
virtualenv nome_da_virtualenv
```

2. Ative a máquina virtual
```
.\nome_da_virtualenv\Scripts\activate
```

3. Instale as dependências do projeto:

```
Pip install -r requirements.txt
```

4. Realize as migrações para o banco de dados:
```
python manage.py makemigrations

Python manage.py migrate
```

5. Crie um super usuário para ter acesso ao sistema 
```
python manage.py createsuperuser
```

6. Inicie o projeto:
```
Python manage.py runserver
```

7. Pronto, agora é só copiar o link do localhost gerado e colocar no navegador (use o usuário e a senha cadastrados previamente para ter acesso a aplicação):
```
localhost:8000
```


