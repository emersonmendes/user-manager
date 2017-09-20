#! /bin/sh
#
##############################################
# Script para configuração da app no heroku
##############################################

# Cria o banco caso não exista
export UM_DATABASE="user-manager.db"
python db.py

# Inicializa a app
python run.py --port $PORT