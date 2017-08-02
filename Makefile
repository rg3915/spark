gen_env:
	python contrib/secret_gen.py

migrate:
	python manage.py migrate

createuser:
	python manage.py shell < shell/create_user.py

create_courses:
	python manage.py shell < shell/create_courses.py

create_classes:
	python manage.py shell < shell/create_classes.py

create_lectures:
	python manage.py shell < shell/create_lectures.py

create_videos:
	python manage.py shell < shell/create_videos.py

selenium_signup:
	python spark/selenium/selenium_signup.py

selenium_event:
	python spark/selenium/selenium_event.py

create: gen_env migrate createuser create_courses create_classes create_videos create_lectures