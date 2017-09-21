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
    - python db.py

# add installed dependencies in requirements.txt

- pip freeze > requirements.txt

# Build (Not done yet)

- [sudo] pip install setuptools
- python setup.py sdist

# Run app

- export UM_DATABASE_HOST="localhost"
- export UM_DATABASE_NAME="usermanager"
- export UM_DATABASE_USER="user"
- export UM_DATABASE_PASS="pass"  

- python run.py --debug True

# Run tests

- export UM_DATABASE_HOST="localhost"
- export UM_DATABASE_NAME="usermanager_test"
- export UM_DATABASE_USER="user"
- export UM_DATABASE_PASS="pass"  

- python tests.py