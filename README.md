# Olist Library - Work at Olist
This project was developed to participate in Olist's recruitment.

# Requirements
* Python 3.8.1
* Windows 10 (this project was developed in W10, so the command lines are from CMD, but is easy to "translate" to Linux)
* A virtual enviroment

# Steps:
## 1 - Install the requirements.txt
a. Download or clone the project into your preferred folder. 
b. In a CMD, browse to your folder.
c. Create/Activate the virtual enviroment. [How To](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
d. Install the "requirements.txt"
```
py -m pip install -r requirements.txt
```

## 2 - Django Migrate
a. Run the migrations
```
py manage.py migrate
```
## 3 - Import Authors
a. Run the custom command
```
py manage.py import_authors authors.csv
```
- NOTE: you can import your own authors using a .csv file 

## 4 - Run tests
a. Run the tests
```
py manage.py test
```
b. Check if the tests passed, must return this message (or similar):
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........................
----------------------------------------------------------------------
Ran 26 tests in 15.270s

OK
Destroying test database for alias 'default'...
```

## 5 - Create a superuser
a. Run the command:
```
py manage.py createsuperuser
```
b. Answer the questions and memorize your user/password

## 6 - Run server and login
a. Run the command:
```
py manage.py runserver
```
b. Answer the questions and memorize your user/password

