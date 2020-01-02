# Learn-django

Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit. Django's primary goal is to ease the creation of complex, database-driven websites.

### Installing on Ubuntu for this project

#### Create a folder as your wish and enter into it
[$ mkdir learn-django]
[$ cd learn-django]

#### Set up virtual environment
[$ virtualenv -p python3 .]

#### To activate virtual env
[$ source bin/activate]

#### Installing Django
[$ pip install django==3.0.1]

#### Check django
[$ pip freeze]

#### Create source folder and enter into it
[$ mkdir src]
[$ cd src]

#### Create configuration folder
[$ django-admin startproject trydjango .]

#### Open a new tab in same derectory and start the server
[$ source bin/activate]
[$ cd src]
[$ python manage.py runserver]

#### To deactivate virtual env
[$ deactivate]
