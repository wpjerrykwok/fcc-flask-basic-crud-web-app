\# Notes for implementation and deployment

Tutorial: Learn Flask for Python - Full Tutorial [YouTube](https://youtu.be/Z1RJmh_OqeA) from [freeCodeCamp.org](https://www.youtube.com/@freecodecamp)

## pre-requisites
* git : https://git-scm.com/downloads
* vscode : https://code.visualstudio.com/download
* gitHub : https://github.com/
* azure : https://portal.azure.com/

## Enviroment setup
1. vscode -> open project folder -> open terminal as bash
2. install virtualenv `pip3 install virtualenv`
3. create env `python3 -m virtualenv -p python3.8 myenv`
   * `-p python3.8` is used to specify a python version
4. activate env `source myenv/Scripts/activate`
   * note `(myenv)` in terminal
5. install Flask `pip3 install flask`
6. install Flask-SQLAlchemy `pip3 install flask-sqlalchemy`
7. install gunicorn `pip3 install gunicorn`

## Build the app
1. follow the tutorial
2. to run the app
   1. open project folder
   2. open terminal
   3. activate `myenv`
   4. run `python app.py` 
   5. `Ctrl-C` to terminate the app
3. to create database `test.db`
   1. open project folder
   2. open terminal
   3. activate `myenv`
   4. run `python` to change to python shell
   5. run `from app import app, db` in python shell
   6. run `app.app_context().push()` in python shell
   7. run `db.create_all()` in python shell
   8. note a folder called `instance` is created automatically with `test.db` inside

## Deploy
1. create the environment requirement list
   1. open project folder
   2. open terminal
   3. activate `myenv`
   4. run `pip3 freeze > requirements.txt`
   5. note a file `requirements.txt` is created
2. push the project to github
3. open azure portal
4. create `Web App` under `App Services`
5. choose github and the project respository as source
6. github will create `Actions` automatically to build and deploy
7. wait and visit yourchoice.azurewebsites.net for the web app
