 
# Flask Forum [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)


This application can be used as **starter kit** if you want to get started building a fullstack application with the framework **Flask**. 
This is a classic forum using features like registration and signing in,  managing threads, commenting, searching threads, like threads and replies, mark replies as best and many other feature which can be found in most web applications.


## Technologies

### Frontend

* [Bootstrap 4](https://getbootstrap.com) - Bootstrap is the most used CSS framework.
* [Vue JS](https://vuejs.org/) - The Progressive JavaScript Framework  for building great user interfaces.
* Other front-end library will be found in a package.json file.

### Backend

* Python 3.7
* SQLite3 for development and MySQL for production.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - A Python Micro-Framework
* Other Python librairies used in the project can be found in the requirements.txt file

## Features

* CRUD (create / read / update / delete) on threads.
* CRUD (create / read / update / delete ) on replies.
* Mark replies as best by the thread's owner.
* Like threads for authenticated users
* Favorite replies for authenticated users
* Pagination on threads listing
* Searching on threads
* Registration with confirmation mails

## Prerequisites

* Python (3.6 or above)
* SQLite3
* Git
* Composer
* Npm (or Yarn)

## Installing / Getting started

* Clone the project from Github

```shell
    $ git clone https://github.com/juvpengele/flask-forum.git
    $ cd flask-forum
```

* Create the .env file:

```shell
    $ cp .env.example .env
```

In the .env file, there are config related to the database and mail that must be added.

* Create the virtual environment file. I use virtualenv for the example but you are free to use any
other tool to create your virtualenv:

```shell
    $ virtualenv venv
    $ . venv/bin/activate
```

* Install dependencies from requirements.txt file

```shell
    $ pip install -r requirements.txt
```

*   Seeds required data to the database

```shell
    $ flask seed run --root="forum/database/seeds"
```

*   Start the development server

```shell
    $ flask run
```

## Licensing

MIT
