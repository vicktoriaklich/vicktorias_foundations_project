from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/smart_closet', echo=True)

Base = declarative_base()  

Session = sessionmaker(bind=engine)

session = Session()


class Items(Base):
	__tablename__ = "Items"
	id = Column(Integer, primary_key=True)
	categories_id = Column(Integer, ForeignKey("Categories.id"))
	brand_id = Column(Integer, ForeignKey("Brands.id"))
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

	def __repr__(self):
		return "<Brands(name='%s', information='%s', link='%s')>" % (self.name, self.information, self.link)

class Comments(Base):
	__tablename__ = "Comments"
	id = Column(Integer, primary_key=True)
	first_name = Column(String)
	comment = Column(String)