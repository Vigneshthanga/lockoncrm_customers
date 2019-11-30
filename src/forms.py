'''
Form UI Classes for the Account and Contact Operations

Author: Kevin Lai
'''
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, Email

class ContactForm(FlaskForm):
	first_name = StringField('first_name',
							  validators=[InputRequired(), Length(min = 1, max = 50)])
	last_name = StringField('last_name',
							  validators=[InputRequired(), Length(min = 1, max = 50)])
	phone_number = IntegerField('phone_number', validators=[InputRequired()])
	email_address = StringField('email_address',
							  validators=[InputRequired(), Email(message='INVALID_EMAIL_ADDRESS'), Length(min = 1, max = 256)])
	street_address = StringField('street_address', validators=[Length(max = 100)])
	city = StringField('city', validators=[Length(max = 60)])
	state = StringField('state',validators=[Length(max = 50)])
	postal_code = IntegerField('postal_code')
	country = StringField('country', validators=[Length(max = 55)])
	notes = TextAreaField('notes')
	save = SubmitField('Save')

class AccountForm(FlaskForm):
	name = StringField('first_name',
						validators=[InputRequired(), Length(min = 1, max = 50)])
	phone_number = IntegerField('phone_number',
							  validators=[InputRequired()])
	email_address = StringField('email_address',
							  validators=[InputRequired(), Email(message='INVALID_EMAIL_ADDRESS'), Length(min = 1, max = 256)])
	street_address = StringField('street_address', validators=[InputRequired(), Length(max = 100)])
	city = StringField('city', validators=[InputRequired(), Length(max = 60)])
	state = StringField('state',validators=[InputRequired(), Length(max = 50)])
	postal_code = IntegerField('postal_code', validators=[InputRequired()])
	country = StringField('country', validators=[InputRequired(), Length(max = 55)])
	notes = TextAreaField('notes')	
	save = SubmitField('Save')
