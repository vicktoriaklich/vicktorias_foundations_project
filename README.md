--- SMART Closet ---

My Foundation Semester Project is a landing page that advertises my product "SMART Closet" and - presented as MVP - collects information on the extent to which the idea is accepted. You can find more information on the landing page itself.

So, what does the project do?
This is a landing page built with the Python Microframework FLASK. There are four main pages: Home, About, Upload and Contact.

Architecture:
- Frontend -
* HTML
* Jinja (Template Engine FLASK)
* CSS

- Backend -
* Python
* FLASK
* MYSQL
____

in order to have a look at the website, you need to install FLASK and an virtual environment.
Download github repository and start local server via console.
____

What can the Landingpage do so far?
- Request for information on a brand at input and submission
- Add and read comments / feedback
- MVP : Upload information and see in table form what has already been stored in the database.
- Contact Form if you are interested as e-mail to Vicktoria Klich


Changes & Process:

Originally I only wanted to offer a login / registration window, so that the potential buyer can always stay informed. After that a contact form made more sense, because the information can be scaled and evaluated. 
In order to give the user a feeling for the value of the end product, I added two functions:
1. querying so-called "label" ratings in connection with the production route of large brands. (Awarness for environment and sustainability)
2. upload possibility. The organized wardrobe includes tables. 

Furthermore I am open for any feedback and would like to give everyone the possibility to let any thoughts run free (comments).

On the whole, I have worked hard on content and frontend, because - if this is in the background for the assessment - it is also in the eye of the viewer to evaluate the functionality of a product.

I switched from SQLite to MySQL because I wanted to use Foreign Keys to connect multiple tables. The additional tables were created with the idea to give the user information if she or he asks for it and to store various items and comments in a database. For the communication I used SQLAlchemy. 

All further details about function and history can be found as comments in the code.
