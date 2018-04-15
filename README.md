# blog.adamzerella
> Source for my personal blogging website.
[![Build Status](https://travis-ci.org/adamzerella/blog.adamzerella.svg?branch=master)](https://travis-ci.org/adamzerella/blog.adamzerella)

### Prerequisites
*   [Python >=3.6](https://www.python.org/downloads/)
*   [Python mysqlclient >=1.3](https://pypi.python.org/pypi/mysqlclient)
*   [Django >=2](https://www.djangoproject.com/download/)
*   [MySQL >=5.7](https://dev.mysql.com/downloads/mysql/)
*   [Apache httpd >=2.4](https://httpd.apache.org/)
*   [mod_wsgi >=4.6](http://modwsgi.readthedocs.io/en/develop/installation.html)
---

### Install
```git
git clone https://github.com/adamzerella/blog.adamzerella
cd ./blog.adamzerella/
```

### Database
Login to the MySQL instance with the temporary password generated upon install and perform the following commands to reset the password and create a database.
```shell
$ mysql -u root -p
```

```sql
ALTER USER "<USER>"@"localhost" IDENTIFIED BY "<PASSWORD>";
CREATE DATABASE blogadamzerella;
USE blogadamzerella;
```

### Environment
```shell
export BAZ_SQL_USER="DB_USER"                             #Database user account
export BAZ_SQL_PASS"DB_PASSWORD"                          #Database user password
export BAZ_SQL_PORT="3306"                                #Database port
export BAZ_DEBUG="False"                                  #Application mode
export BAZ_SECRET_KEY="key"                               #Trusted key
export BAZ_ALLOWED_HOSTS="'[::1]', '127.0.0.1', ... "     #Whitelisted hosts
export BAZ_STATIC_ROOT="/var/www/example.com/static/"     #Static content loc
```

### Setup app
```python
python manage.py migrate                        #Initialise database tables
python manage.py loaddata blog subscribers      #load mock data
python manage.py createsuperuser                #Create admin account
```

### Run Locally
```python
python manage.py runserver
```
> Server should then be running @ http://127.0.0.1:8000

### Test
```python
python -Wall manage.py test app
```

### Deployment
```
```
