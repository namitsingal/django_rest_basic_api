setup:
	virtualenv ./venv
	./venv/bin/pip install -r requirements.txt
	./venv/bin/python manage.py migrate
run:
	./venv/bin/python manage.py runserver 0.0.0.0:80

