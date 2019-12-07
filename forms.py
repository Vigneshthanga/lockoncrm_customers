'''
Form UI Classes for the Account and Contact Operations
Author: Kevin Lai
'''
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
#from wtforms import InputField
# InputField validator does not work with AutoComplete data
# Use InputField validator for secondary confirmation, like to confirm email

class ContactForm(FlaskForm):
	fname = StringField('first_name', validators=[DataRequired(), Length(min = 1, max = 100)])
	lname = StringField('last_name', validators=[DataRequired(), Length(min = 1, max = 100)])
	account_id = IntegerField('account_id', validators=[DataRequired()])
	pnumber = IntegerField('phone_number', validators=[DataRequired()])
	email = StringField('email_address', validators=[DataRequired(), Email(message='INVALID_EMAIL_ADDRESS'), Length(min = 1, max = 256)])
	street = StringField('street_address', validators=[Length(max = 100)])
	city = StringField('city', validators=[Length(max = 100)])
	state = StringField('state',validators=[Length(max = 100)])
	postal = IntegerField('postal_code')
	country = StringField('country', validators=[Length(max = 100)])
	notes = TextAreaField('notes')
	save = SubmitField('Save')

class AccountForm(FlaskForm):
	name = StringField('first_name',
						validators=[DataRequired(), Length(min = 1, max = 100)])
	pnumber = IntegerField('phone_number', validators=[DataRequired()])
	email = StringField('email_address', validators=[DataRequired(), Email(message='INVALID_EMAIL_ADDRESS'), Length(min = 1, max = 256)])
	street = StringField('street_address', validators=[DataRequired(), Length(max = 100)])
	city = StringField('city', validators=[DataRequired(), Length(max = 100)])
	state = StringField('state',validators=[DataRequired(), Length(max = 100)])
	postal = IntegerField('postal_code', validators=[DataRequired()])
	country = StringField('country', validators=[DataRequired(), Length(max = 100)])
	notes = TextAreaField('notes')	
	save = SubmitField('Save')