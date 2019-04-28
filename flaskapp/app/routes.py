from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail
from db import *

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'vicktoria.klich@code.berlin'
app.config["MAIL_PASSWORD"] = 'somebodylikeme'
 
mail.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		brand = session.query(Brands).filter(Brands.name == request.form["search_brand"])
		return render_template('home.html', brand=brand)
	return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
	#comments databse query
	return render_template('about.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():

	items = session.query(Items).order_by(Items.id).all()
	category = session.query(Categories)
	brands = session.query(Brands)


	if request.method == "POST":
		item = Items(name=request.form["name"],categories_id=request.form["category"], brand_id=request.form["brand"], description=request.form["description"], season=request.form["season"])

		session.add(item)
		session.commit() 
		return render_template('upload.html', category=category, brands=brands, items=items)
	return render_template('upload.html', items=items, category=category, brands=brands)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if request.method == 'POST':

		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', form=form)
		else:
			msg = Message(form.subject.data, sender='vicktoria.klich@code.berlin', recipients=['klichvictoria@googlemail.com'])
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)

		return render_template('contact.html', success=True)

	elif request.method == 'GET':
		return render_template('contact.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)