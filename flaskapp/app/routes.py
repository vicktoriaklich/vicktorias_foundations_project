
#--This Python file defines the routes--#


#import flask framework with render_template (=> returning HTML templates), request (=> wether the current method is a GET or a POST), and flash (=> messages for the user)
from flask import Flask, render_template, request, flash
# import ContactForm and Flask Mail so I will receive a Message from a potential user who puts in his/her E-Mail. Flask Mail allows to send emails from Flask app
from forms import ContactForm
# message class to compose a new email and Mail class to send the email
from flask_mail import Message, Mail
# importing everything from the database I work with
from db import *

# mail variable that contain a usable instance of Mail class
mail = Mail()

#creating instance of the Flask class
app = Flask(__name__)

# secret key where Flask WTF takes care of generating and managing unique tokens for my form
# useful to avoid someone submitting information to my sever from another website
app.secret_key = 'development key'

# configure Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'vicktoria.klich@code.berlin'
app.config["MAIL_PASSWORD"] = 'somebodylikeme'
 
# attach mail to my Flask app so I can start using it
mail.init_app(app)


# route to home page
@app.route('/', methods=['GET', 'POST'])
def home():

# Displays Mission Statement and general advertisement for future product (not launched yet)
# Home Page.
# Bottom: if statement for POST request. User can choose between Brands to receive information out of database Brands

	if request.method == "POST":
		# if POST request then session starts to filter within Brands Table for a row in which the brands name equals assigned information
		brand = session.query(Brands).filter(Brands.name == request.form["search_brand"])
		# afterwards returns template home with defined brand
		return render_template('home.html', brand=brand)
	# if no POST request then only home template without further information for brand
	return render_template('home.html')


# route to about page, where user receives more information about the project and is able to add and see comments
@app.route('/about', methods=['GET', 'POST'])
def about():
	# user sends POST request with submitting first name and column values into database
	if request.method == "POST":
		comment = Comments(first_name=request.form["first_name"], text=request.form["text"])
		session.add(comment)
		session.commit()
	# Comments Table will be displayed (outside of if statement to avoid double code)
	comments = session.query(Comments).order_by(Comments.id).all()
	return render_template('about.html', comments=comments)


# MVP where user can upload Items (stored in table), with methods GET and POST
@app.route('/upload', methods=['GET', 'POST'])
def upload():
# within function Items that are already in the database shall be displayed.
# here we have three Tables where the table Items has the Foreign Keys and therefore a connection to Brands and Categories
# sessions basically establishes all conversation with the database

	# if user fills out fields and selects radio buttons a POST request occurs
	if request.method == "POST":
		# input will be assigned to Items table with request.form
		# categories_id and brand_id are Foreign Keys -> user can select displayed name related to ID
		item = Items(name=request.form["name"],categories_id=request.form["category"], brand_id=request.form["brand"], description=request.form["description"], season=request.form["season"])
		# items stored with session
		session.add(item)
		# session needs to be commited in order to store in database
		session.commit()
 
	# three tables Items, Categories and Brands will be displayed connected
	items = session.query(Items).order_by(Items.id).all()
	category = session.query(Categories)
	brands = session.query(Brands)
	return render_template('upload.html', items=items, category=category, brands=brands)

# Contact Form to fill out if interested
@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	# if server receives POST request, function form.validate() should capture the form field data and check if it's valid
	if request.method == 'POST':
	# if any validation check fails, form.validate() will be False.
		if form.validate() == False:
			# flash message occurs
			flash('All fields are required.')
			# after flash message template will be returned
			return render_template('contact.html', form=form)
		# esle statement if no validation error occurs
		else:
			msg = Message(form.subject.data, sender='vicktoria.klich@code.berlin', recipients=['klichvictoria@googlemail.com'])
			# send the email using % as a formatting operator (users name, email and message)
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			# send email via mail.send(msg)
			mail.send(msg)
		# return template with sucess message
		return render_template('contact.html', success=True)
	# return template with contact form (GET request)
	elif request.method == 'GET':
		return render_template('contact.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)