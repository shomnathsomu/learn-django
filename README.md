# Learn-django

Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit. Django's primary goal is to ease the creation of complex, database-driven websites.

### Running commands for this project on Ubuntu

#### Open a terminal and enter the commands onto it

$ git clone https://github.com/shomnathsomu/learn-django.git

$ cd learn-django/

#### Set up virtual environment

$ sudo apt install python3-virtualenv
$ virtualenv -p python3 .

#### To activate virtual env

$ source bin/activate

#### Installing Django

$ pip install django==3.0.1

#### Check django

$ pip freeze

#### Apply the migrations for app(s):

$ cd src

$ python manage.py migrate

#### Create a superuser for admin

$ python manage.py createsuperuser

#### Open a new terminal in the project directory and start the server

$ source bin/activate

$ cd src

$ python manage.py runserver

#### To deactivate virtual env

$ deactivate
