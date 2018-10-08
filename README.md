Preaparing for database. Use postgres 9.6
```
sudo -u postgres psql

create database trash;
create user trash with password trash;
grant all privileges on database trash to trash;
```
