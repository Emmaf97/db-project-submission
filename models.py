from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import  Column, Integer, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(5), nullable=False)
    lname = db.Column(db.String(5), nullable=False)
    address = db.Column(db.String(5), nullable=False)
    user_account_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    
class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    user = db.relationship('User', backref='account', uselist=False)
    
class UserComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(80), nullable=False)
    
class UserItemList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(80), nullable=False)
    
    
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productSize = db.Column(db.String(80), nullable=False)
    productQuantity = db.Column(db.Integer, nullable=False)
    productType = db.Column(db.String(1), unique=True, nullable=False)
    productUserLiked = db.Column(db.String(2), unique=True, nullable=False)
    
    