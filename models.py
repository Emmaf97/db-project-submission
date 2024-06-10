from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import  Column, Integer, Text, TIMESTAMP
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(5), nullable=False)
    lname = db.Column(db.String(5), nullable=False)
    address = db.Column(db.String(5), nullable=False)
    
class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    
class UserComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), unique=True, nullable=False)
    time = db.Column(db.String(80), unique=True, nullable=False)
    comment = db.Column(db.String(80), unique=True, nullable=False)
    
class UserItemList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), unique=True, nullable=False)
    time = db.Column(db.String(80), unique=True, nullable=False)
    comment = db.Column(db.String(80), unique=True, nullable=False)
    
    
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productSize = db.Column(db.String(80), unique=True, nullable=False)
    productQuantity = db.Column(db.Integer, unique=True, nullable=False)
    productType = db.Column(db.String(1), unique=True, nullable=False)
    productUserLiked = db.Column(db.String(2), unique=True, nullable=False)
    
    