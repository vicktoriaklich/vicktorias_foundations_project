# database file
# connection & communication to the database MySQL
# SQLAlchemy as an Object Relational Mapper (or in my words: Translator between Python and MySQL Table)

# import all sqlalchemy modules needed
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# ORM & Session
# Object-relational mapper written in object oriented language (such as Python in that case) which translates Python Objects in SQL codes
from sqlalchemy.orm import sessionmaker
# importing datatypes and FK for connection between Tables
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

# MySQL dialect will interpret instructions to the Python built-in pymysql module
# SQLAlchemy loggin in port
engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/smart_closet', echo=True)

# Base => declare own classes for tables
Base = declarative_base()  

# important as something like a "middleman" between routes.py and database (communication)
Session = sessionmaker(bind=engine)

session = Session()


# all database tables defined with same structure
class Items(Base):
	# equals Table name
	__tablename__ = "Items"
	# id column defined as PK
	id = Column(Integer, primary_key=True)
	# FK (PK Categories Table)
	categories_id = Column(Integer, ForeignKey("Categories.id"))
	# FK (PK in Brands Table)
	brand_id = Column(Integer, ForeignKey("Brands.id"))
	# following columns defined with datatype String
	name = Column(String)
	description = Column(String)
	season = Column(String)


class Categories(Base):
	__tablename__ = "Categories"
	id = Column(Integer, primary_key=True)
	name = Column(String)

class Brands(Base):
	__tablename__ = "Brands"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	information = Column(String)
	link = Column(String)
	# returns columns
	def __repr__(self):
		return "<Brands(name='%s', information='%s', link='%s')>" % (self.name, self.information, self.link)

class Comments(Base):
	__tablename__ = "Comments"
	id = Column(Integer, primary_key=True)
	first_name = Column(String)
	text = Column(String)