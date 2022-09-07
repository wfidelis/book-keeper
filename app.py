from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


#SQLAlchemy Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return "<p>Hello, Universe!</p>"


# if __name__ == '__main__':
#     db.create_all()
#     db.session.commit()
# 

