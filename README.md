# Eventex

Sistema de Eventos do [WTTD](http://welcometothedjango.com.br/).


## Como desenvolver?

1. Clone o Repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:fabiofa87/Eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como Fazer Deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
```

https://eventex-fabiofaria.herokuapp.com/ 

## Em Desenvolvimento