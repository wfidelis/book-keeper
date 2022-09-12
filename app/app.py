from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, requests, json
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

#SQLAlchemy Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
db = SQLAlchemy(app)


api_url = "https://www.googleapis.com/books/v1/volumes"

parameters = {
    'q': "Harry Potter", 
    "key": os.getenv('GOOGLEBOOKS_API_KEY'),
    'inauthor' : 'Rowling'
}

response = requests.get(api_url, params=parameters)
books = response.json()


@app.route('/')
def home():
    return 'I am well frfrfr'


from models import *

db.create_all()
db.session.commit()