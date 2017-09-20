# user-manager

- User manager rest api in python

# install

- install virtualenv
    - [sudo] pip install virtualenv

- create virtual environment
    - virtualenv user-manager-env
    
- activate virtual environment
    - source user-manager-env/bin/activate

- install dependencies:
    - pip install -r requirements.txt

- create database:
    - export UM_DATABASE="user-manager.db"  
    - python db.py

# run app

- activate virtual environment
    - source user-manager-env/bin/activate

- export UM_DATABASE_HOST="localhost"
- export UM_DATABASE_NAME="usermanager"
- export UM_DATABASE_USER="root"
- export UM_DATABASE_PASS="root"  

- python run.py

# add installed dependencies in requirements.txt

- pip freeze > requirements.txt

# Build (Not done yet)

- [sudo] pip install setuptools
- python setup.py sdist