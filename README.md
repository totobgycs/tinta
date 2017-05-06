# Setup
Pre-requisites: git, python3, rabbitmq installed system-wide

clone the project (will create a directory)
    git clone git@github.com:totobgycs/tinta.git

cd into the project dir
    cd tinta

create the python env
    virtualenv -ppython3 env

activate the python env
    source env/bin/activate

install dependencies into the env
    pip install -r requirements.txt

create a dev sqllite database
    python manage.py migrate

start the dev server
    python manage.py runserver 0:8080


