from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Float, create_engine

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable = False)
    job_title = Column(String(150), nullable = False)
    salary = Column(Float, nullable = False)

    def __repr__(self):
        return f'[id = {self.id}, name = {self.name}, job_title = {self.job_title}, salary = {self.salary}]'
    
#setup database

engine = create_engine('sqlite:///employees_db.sqlite', echo=True) #create database if not exist

Base.metadata.create_all(engine) #create the table for model classes


# setup things for transaction (crud opd)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


#crud ops 

virat = Employee(name = 'Virat' , job_title = 'Circketer', salary = 120000)
session.add(virat)

millar = Employee(name = 'Millar' , job_title = 'Circketer', salary = 100000)
session.add(millar)

dhoni = Employee(name = 'Dhoni' , job_title = 'Circketer', salary = 50000)
session.add(dhoni)

employee = session.query(Employee).all()
print(employee)

millar = session.query(Employee).filter_by(name = 'Millar').first()
print(millar)

dhoni.salary = 100000

session.delete(millar)
session.commit()