# user-manager

- User manager rest api in python

# install

- [sudo] pip install virtualenv
- virtualenv venv
- source venv/bin/activate
- pip install -r requirements.txt

# run app

- source venv/bin/activate
- python run.py


# POST Example

- curl -H "Content-Type: application/json" -X POST --data @teste.json http://localhost:5000/users

# add installed dependencies in requirements.txt

- pip freeze > requirements.txt
