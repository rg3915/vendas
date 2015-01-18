install:
	pip install -r requirements.txt
	pip uninstall pyparsing
	pip install -Iv https://pypi.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz#md5=9be0fcdcc595199c646ab317c1d9a709
	pip install pydot
	pip freeze > requirements.txt

mer:
	./manage.py graph_models -e -g -l dot -o modelagem/vendas.png vendas

heroku:
	git push heroku master

herokumigrate:
	heroku run ./manage.py migrate

herokureset:
	heroku pg:reset DATABASE
	heroku run ./manage.py syncdb --noinput
	heroku run ./manage.py loaddata vendas_project/dados/fixtures_bkp.json	