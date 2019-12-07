'''
This file performs the following:

1. Handles the routing between the different pages for the creation and viewing of accounts and contacts.

Author: Kevin Lai
'''
from flask import Flask, render_template, redirect, url_for
from forms import ContactForm, AccountForm
from models import db, Account, Contact
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
#app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://customers:[db_password]@0.0.0.0:[db_port_number]/customers"

# Production MySQL DB - Use This!!!
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://customers:commonsyspass@192.168.33.15:3306/customers"

# Only for testing on localhost
#app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://customers:kevin123@localhost:5432/customers"

# Only for local database. DO NOT use for production. ONLY use for development and testing.
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///customers.db"

db.init_app(app)
with app.app_context():
    db.create_all()

# Only for testing purposes
@app.route("/customers/")
@app.route("/customers/home/")
def homepage():
	return render_template('home.html')

@app.route("/customers/contacts/", methods=['GET','POST'])
def view_contact():
	contacts_list = Contact.query.all()
	return render_template("view_contact.html", contacts_list = contacts_list)

@app.route("/customers/contacts/create/", methods=['GET','POST'])
def create_contact():
	form = ContactForm()
	completion_msg = ""
	if form.validate_on_submit():
		if form.save.data:
			new_contact = Contact(fname = form.fname.data, lname = form.lname.data,
								  account_id = form.account_id.data,				
								  pnumber = form.pnumber.data, email = form.email.data,
								  street = form.street.data, city = form.city.data,
								  state = form.state.data, postal = form.postal.data,
								  country = form.country.data, notes = form.notes.data)
			db.session.add(new_contact)
			try:
				db.session.commit()
			except:
				completion_msg = "Failed to create contact. Please try again."
			if completion_msg == "":
				completion_msg = "Success! The contact has been saved."
				return redirect(url_for('view_contact'))
		else:			
			completion_msg = "Failed to create contact. Please try again."
	return render_template("create_contact.html", form = form, completion_msg = completion_msg)


@app.route("/customers/contacts/<int:contact_id>/edit/", methods=['GET','POST'])
def edit_contact(contact_id):
	contact = Contact.query.get_or_404(contact_id)
	form = ContactForm(obj=contact)
	completion_msg = ""
	if form.validate_on_submit():
		if form.save.data:
			contact.fname = form.fname.data
			contact.lname = form.lname.data
			contact.account_id = form.account_id.data
			contact.pnumber = form.pnumber.data
			contact.email = form.email.data
			contact.street = form.street.data
			contact.city = form.city.data
			contact.state = form.state.data
			contact.postal = form.postal.data
			contact.country = form.country.data
			contact.notes = form.notes.data
			try:
				db.session.commit()
			except:
				completion_msg = "Failed to create contact. Please try again."
			if completion_msg == "":
				completion_msg = "Success! The contact has been saved."
				return redirect(url_for('view_contact'))
		else:			
			completion_msg = "Failed to create contact. Please try again."
	return render_template("edit_contact.html", form = form, completion_msg = completion_msg)

@app.route("/customers/contacts/<int:contact_id>/delete/", methods=['GET','POST'])
def delete_contact(contact_id):
	contact = Contact.query.get_or_404(contact_id)
	db.session.delete(contact)
	db.session.commit()
	return redirect(url_for('view_contact'))

@app.route("/customers/accounts/", methods=['GET','POST'])
def view_account():
	accounts_list = Account.query.all()
	return render_template("view_account.html", accounts_list = accounts_list)


@app.route("/customers/accounts/create/", methods=['GET','POST'])
def create_account():
	form = AccountForm()
	completion_msg = ""
	if form.validate_on_submit():
		if form.save.data:
			new_account = Account(name = form.name.data, pnumber = form.pnumber.data,
								  email = form.email.data, street = form.street.data,
								  city = form.city.data, state = form.state.data,
								  postal = form.postal.data, country = form.country.data,
								  notes = form.notes.data)
			db.session.add(new_account)
			try:
				db.session.commit()
			except:
				completion_msg = "Failed to create account. Please try again."
			if completion_msg == "":
				completion_msg = "Success! The account has been saved."
				return redirect(url_for('view_account'))				
		else:
			completion_msg = "Failed to create account. Please try again."
	return render_template("create_account.html", form = form, completion_msg = completion_msg)

@app.route("/customers/accounts/<int:account_id>/view_account_contacts/", methods=['GET','POST'])
def view_account_contacts(account_id):
	account = Account.query.get_or_404(account_id)
	return render_template("view_account_contacts.html", contacts_list = account.contacts)	

@app.route("/customers/accounts/<int:account_id>/edit/", methods=['GET','POST'])
def edit_account(account_id):
	account = Account.query.get_or_404(account_id)
	form = AccountForm(obj=account)
	completion_msg = ""
	if form.validate_on_submit():
		if form.save.data:
			account.name = form.name.data
			account.pnumber = form.pnumber.data
			account.email = form.email.data
			account.street = form.street.data		
			account.city = form.city.data
			account.state = form.state.data
			account.postal = form.postal.data
			account.country = form.country.data
			account.notes = form.notes.data
			try:
				db.session.commit()
			except:
				completion_msg = "Failed to update account. Please try again."
			if completion_msg == "":
				completion_msg = "Success! The account has been saved."
				return redirect(url_for('view_account'))			
		else:			
			completion_msg = "Failed to update account. Please try again."
	return render_template("edit_account.html", form = form, completion_msg = completion_msg)

@app.route("/customers/accounts/<int:account_id>/delete/", methods=['GET','POST'])
def delete_account(account_id):
	account = Account.query.get_or_404(account_id)
	db.session.delete(account)
	db.session.commit()
	return redirect(url_for('view_account')) 

if __name__ == '__main__':
	app.run(debug=True)
