"""
-- using a Python form for my Contact Form / Page --
"""
# install and import Flaks-WTF. Handles and validates form data
from flask_wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms import validators, ValidationError

# creating class named ContactForm, inheriting from the base Form class
class ContactForm(Form):
	# creating each field that the user should see and fill out in the contact form
	# if any validation check fails, the contact page should reloud with an error message
	name = TextField("Name",   [validators.Required()])
	email = TextField("Email",   [validators.Required(), validators.Email()])
	subject = TextField("gender / sex",   [validators.Required()])
	message = TextAreaField("Reason",   [validators.Required()])
	submit = SubmitField("Send")

	# I will receive EMAIL and will be able to track and scale the reasons