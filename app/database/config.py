from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import URL_DB

Base = declarative_base()

engine = create_engine(URL_DB)
Session = sessionmaker(bind=engine)
