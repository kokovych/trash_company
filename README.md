## Company with personal account
 
 Example of some company with personal account. SPA.
 
 **Backend part** :
 
 - API - Django rest framework, django 2.1, python 3.6;
 - Database - postgres 9.6;
 
 
 **Frontend part** :
 - Angular 6 (typescript);
 - Webpack - I used webpack for converting all angular part to few js files for my template;


### Database
1) Preaparing for database. Use postgres 9.6
```
~$ sudo -u postgres psql

create database trash;
create user trash with password trash;
grant all privileges on database trash to trash;
```
Note: you can choose DB password, user etc in `trash/settings.py` in dictionary `DATABASES`.

2) Apply all migrations to database:
```
~$ python manage.py migrate
```


### Frontend part
Requirements: npm, webpack.

Frontend is created with angular 6. Frontend working directory is `frontend_angular`.

With webpack files from `frontend_angular` convert to js into `staicfiles`. Can change in `webpack.conf.js`.

Open `frontend_angular` and run:
 - ```npm install``` - will create `node_modules` directory in `frontend_angular`;
 - ```webpack``` or ```npm run build``` - will create few js files in directory `staticfiles`


##### Test API

Testing via Django.

```
~$ python manage.py test
```
