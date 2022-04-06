import datetime
from email.policy import default
from traceback import print_exc
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/Item?user=postgres&password=@gk11051996@'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True    
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    std = db.Column(db.Integer, unique=False, nullable=False)
    regno = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, std, regno):
        self.name = name
        self.std = std
        self.regno = regno
db.create_all()  

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    author = db.Column(db.String(100), unique=False, nullable=True)
    price = db.Column(db.Numeric(10,2), unique=False, nullable=True)
    maxcount = db.Column(db.Integer, unique=False, nullable=True)
    curstock = db.Column(db.Integer, unique=False, nullable=True)

    def __init__(self, name, author, price,maxcount,curstock):
        self.name = name
        self.author = author
        self.price = price
        self.maxcount = maxcount
        self.curstock = curstock
db.create_all()

class Summary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookid = db.Column(db.Integer, unique=False, nullable=True)
    studentid = db.Column(db.Integer, unique=False, nullable=True)
    studentname = db.Column(db.String(80), unique=False, nullable=False)
    bookname = db.Column(db.String(100), unique=False, nullable=False)
    getdate = db.Column(db.Date, default=datetime.datetime.utcnow)
    retdate = db.Column(db.Date, nullable=True, default=datetime.datetime.utcnow)
    type = db.Column(db.String(1), nullable=True)

    def __init__(self, bookid, studentid, studentname,bookname,getdate,retdate,type):
        self.bookid = bookid
        self.studentid = studentid
        self.studentname = studentname
        self.bookname = bookname
        self.getdate = getdate
        self.retdate = retdate
        self.type = type
db.create_all()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content 
    db.create_all()               

db.create_all()