from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from employee12 import Base, Employee


    
#setup database

engine = create_engine('sqlite:///employees_db.sqlite', echo=True) #create database if not exist

Base.metadata.create_all(engine) #create the table for model classes


# setup things for transaction (crud opd)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
