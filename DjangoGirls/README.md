# DjangoGirls Tutorial

Familiarizing myself with Django by creating a simple blog following this excellent tutorial: [DjangoGirls Tutorial](https://tutorial.djangogirls.org/en/)

## To start a new Django app:

1. cd into your project directory.
1. in the command prompt, type ```python -m venv myvenv``` where "myvenv" is the name of your virtual environment.
  * Note: the .gitignore template automatically excludes any directory ending with "venv"
1. cd into myvenv directory
1. run the following:```shell . Scripts/activate```
  * You will know the virtual environment is running when the command prompt is preceded with "(myvenv)" (or whatever you named your virtual environment)
1. cd into the project root directory (out of the myvenv directory)
1. run the following command: ```shell django-admin.exe startproject mysite .```
  * "mysite" is the name of your project
  * note the period at the end of the command.

## To Run

1. Clone the repo.
2. From the command line, cd into the root directory (wherever the manage.py file is located).
3. Type ```python manage.py runserver``` into the command line.
4. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
