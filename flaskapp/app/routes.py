from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail
import sqlite3

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'vicktoria.klich@code.berlin'
app.config["MAIL_PASSWORD"] = 'somebodylikeme'
 
mail.init_app(app)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
	if request.method == 'POST':
		entered_comment = request.form['comment']
		conn =sqlite3.connect('contact.db')
		cur = conn.cursor()
		cur.execute("INSERT INTO comments (comment) VALUES ('{}')".format(entered_comment))
		conn.commit()
		cur.execute('SELECT comment FROM comments')
		rows = cur.fetchall()
		return render_template('about.html', comments = rows)
	else:
		conn =sqlite3.connect('contact.db')
		cur = conn.cursor()
		cur.execute('SELECT comment FROM comments')
		rows = cur.fetchall()
		return render_template('about.html', comments = rows)


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
		conn =sqlite3.connect('contact.db')
		cur = conn.cursor()
		cur.execute('SELECT comment FROM comments')
		rows = cur.fetchall()

		return render_template('contact.html', form=form, comments = rows)

if __name__ == '__main__':
	app.run(debug=True)