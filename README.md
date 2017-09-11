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
    - export UM_DATABASE="user_manager.db"  
    - python db.py

# run app

- activate virtual environment
    - source venv/bin/activate
    
- python run.py


# POST Example

- curl -H "Content-Type: application/json" -X POST --data @teste.json http://localhost:5000/users

# add installed dependencies in requirements.txt

- pip freeze > requirements.txt
