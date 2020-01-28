from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



class Comments(Base):
   __tablename__ = 'tomato sauce'
   id = Column(Integer, primary_key=True)
   firstname = Column(String)
   lastname = Column(String)
   comment = Column(String)

