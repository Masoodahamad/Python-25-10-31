from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from product import Base, Product

engine = create_engine("sqlite:///product_db.sqlite", echo = True)

Base.metadata.create_all(engine)

sessionLocal = sessionmaker(bind = engine)
session = sessionLocal()
