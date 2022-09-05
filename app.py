from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#SQLAlchemy Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:*mMN7FnL0]{t@localhost/booksdb'
app.config['SECRET_KEY'] = "x10\xcbb\x00\x94\xccA\xc8\x13\xfc\x89K"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return "<p>Hello, Universe!</p>"


# if __name__ == '__main__':
#     db.create_all()
#     db.session.commit()
# 

