from flask import render_template, redirect, request, url_for
from src.config.db import  createDB, installDB, CONEXION_PATH
from src import app
from os import path
import json
import src.config.globals as globals

@app.route('/')
def index():
    if (globals.DB == False):
        return render_template('setting.html')
    
    return render_template('index.html')

@app.route('/setting', methods=['POST'])
def setting():
   
    dbData = {
        "database": request.form.get('dbName'),
        "user": request.form.get('userName'),
        "password": request.form.get('password'),
        "host": request.form.get('dbServer'),
        "port": int(request.form.get('dbPort')),
    }

    con = open(CONEXION_PATH, 'w')
    con.write(json.dumps(dbData))
    con.close()

    createDB()
    installDB()

    return redirect(url_for('index'))