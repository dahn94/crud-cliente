# crud-cliente

Repositório criado para uma aplicação com o framework Django que realiza o CRUD (Create, Read, Update, Delete) de clientes. Na realização dos testes do projeto foi usado o VENV. Obs: faltando apenas a realização do teste da views da aplicação app. 

<h2> Configuração necessária para rodar o projeto</h2>

1. Após clonar o repositório em seu computador, mova-se para dentro da pasta do projeto e realize a criação de ambiente virtual para rodar a aplicação:
```
python -m venv nome_da_virtualenv
```

2. Ative a máquina virtual
```
.\nome_da_virtualenv\Scripts\activate (No Windows) 
$ source nome_da_virtualenv/bin/activate (bash/zsh)
```

3. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

4. Realize as migrações para o banco de dados:
```
python manage.py migrate
```

5. Crie um super usuário para poder ter acesso ao sistema 
```
python manage.py createsuperuser
```

6. Inicie o projeto:
```
python manage.py runserver
```

7. Pronto, agora é só copiar o link gerado e colocar no navegador (utilize o usuário e a senha cadastrados previamente para ter acesso ao sistema):
```
localhost:8000
```


