install:
	pip install -r requirements.txt

install2:
	pip install -Iv https://pypi.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz#md5=9be0fcdcc595199c646ab317c1d9a709
	pip install pydot
	pip freeze > requirements.txt

migrate:
	./manage.py makemigrations
	./manage.py migrate

createuser:
	./manage.py createsuperuser --username='admin' --email=''

mer:
	./manage.py graph_models -e -g -l dot -o modelling/sales.png sales

heroku:
	git push heroku master

herokumigrate:
	heroku run ./manage.py migrate

herokureset:
	heroku pg:reset DATABASE
	heroku run ./manage.py syncdb --noinput
	heroku run ./manage.py loaddata fixtures.json

backup:
	./manage.py dumpdata --format=json --indent=2 > fixtures.json

load:
	./manage.py loaddata fixtures.json

run:
	./manage.py runserver

get_produtos:
	python vendas/api/get_produtos.py

create_brands:
	./manage.py shell < fixtures/create_brands.py

create_categories:
	./manage.py shell < fixtures/create_categories.py

create_products:
	./manage.py shell < fixtures/create_products.py

create_products2:
	./manage.py shell < fixtures/create_products2.py

create_customers:
	./manage.py shell < fixtures/create_customers.py

create_sellers:
	./manage.py shell < fixtures/create_sellers.py

create_sales:
	./manage.py shell < fixtures/create_sales.py

initial: install migrate createuser

createAll: create_brands create_products2 create_customers create_sellers create_sales
