'''
Account and Contact classes

Author: Kevin Lai
'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
	id = db.Column(db.Integer,primary_key=True, autoincrement=True)
	fname = db.Column(db.String(50),nullable=False)
	lname = db.Column(db.String(50),nullable=False)	
	pnumber = db.Column(db.Integer,nullable=False)	
	email = db.Column(db.String(256),nullable=False)
	street = db.Column(db.String(100))
	city = db.Column(db.String(60))
	state = db.Column(db.String(50))
	postal = db.Column(db.Integer)	
	country = db.Column(db.String(55))
	notes = db.Column(db.Text)
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	def __init__(self,fname,lname,account_id,pnumber,email,street="",city="",state="",postal="",country="",notes=""):
		self.fname = fname
		self.lname = lname
		self.account_id = account_id
		self.pnumber = pnumber
		self.email = email
		self.street = street
		self.city = city
		self.state = state
		self.postal = postal		
		self.country = country
		self.notes = notes	


class Account(db.Model):
	id = db.Column(db.Integer,primary_key=True, autoincrement=True)	
	name = db.Column(db.String(100),nullable=False)
	pnumber = db.Column(db.Integer,nullable=False)	
	email = db.Column(db.String(256),nullable=False)
	street = db.Column(db.String(100),nullable=False)
	city = db.Column(db.String(60),nullable=False)
	state = db.Column(db.String(50),nullable=False)
	postal = db.Column(db.Integer,nullable=False)	
	country = db.Column(db.String(55),nullable=False)
	notes = db.Column(db.Text)
	contacts = db.relationship('Contact', backref="account", lazy=True)
	
	def __init__(self, name, pnumber, email, street, city, state, postal, country, notes=""):
		self.name = name
		self.pnumber = pnumber
		self.email = email
		self.street = street
		self.city = city
		self.state = state
		self.postal = postal
		self.country = country
		self.notes = notes

