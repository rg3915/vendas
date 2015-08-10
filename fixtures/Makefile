delete_migrations:
	rm -rf ../vendas/migrations/
	
reset:
	rm ../db.sqlite3
	python ../../manage.py makemigrations vendas
	python ../../manage.py migrate
	python ../../manage.py createsuperuser --username='admin' --email='admin@admin.com'

load:
	python ../../manage.py loaddata fixtures_bkp.json

backup:
	python ../../manage.py dumpdata --format=json --indent=2 vendas > fixtures_bkp.json