# esterni-pjecalc-crawler

Repositório criado para uma aplicação com o Selenium que realiza a automação do pjecalc numa máquina windows. 

<h2> Configuração necessária para rodar o projeto</h2>

1. Após clonar o repositório em seu computador, mova-se para dentro da pasta do projeto e realize a criação de ambiente virtual para rodar a aplicação:
```
python3 -m venv nome_da_virtualenv
```

2. Ative a máquina virtual
```
.\nome_da_virtualenv\Scripts\activate (CMD/PowerShell) 
```

3. Instale as dependências do projeto:

```
pip install selenium
```

4. Baixe o Geckodriver para Windows e descompacte no diretório C:\GeckoDriver (Usar PowerShell no modo Administrador)

```
Invoke-WebRequest https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-win64.zip -OutFile C:\GeckoDriver\geckodriver-v0.29.1-win64.zip

Expand-Archive C:\GeckoDriver\geckodriver-v0.29.1-win64.zip -DestinationPath C:\GeckoDriver\
```

5. Execute o programa
```
python3 main.py
```
