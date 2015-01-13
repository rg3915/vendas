reset:
	rm ../db.sqlite3
	python ../../manage.py makemigrations vendas
	python ../../manage.py migrate
	python ../../manage.py createsuperuser

load:
	python ../../manage.py loaddata fixtures_bkp.json