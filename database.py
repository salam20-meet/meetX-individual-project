from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from random import *


engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_comment(firstname,lastname,comment ):

	mycomment = Comments(id=randint(0,1000),firstname=firstname,lastname=lastname,comment=comment)
	

	session.add(mycomment)
	session.commit() 

def get_all_comments():
	all_comments = session.query(Comments).all()
	print(all_comments)
	return all_comments

add_comment("firstname","lastname","comment")
"""print (get_all_comments()[0].firstname)"""