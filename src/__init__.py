from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

# importando controladores
from src.controller import *

def create_app():
    app.run(debug=True)