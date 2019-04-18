from flask_wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms import validators, ValidationError

class ContactForm(Form):
	name = TextField("Name",   [validators.Required("Please enter your name.")])
	email = TextField("Email",   [validators.Required(), validators.Email()])
	subject = TextField("gender / sex",   [validators.Required()])
	# will change that to selection
	message = TextAreaField("Reason",   [validators.Required()])
	#insert placeholder example
	submit = SubmitField("Send")

	# I will receive EMAIL and will be able to track and scale the reasons