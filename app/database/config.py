from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

Base = declarative_base()

print(config.URL_DB)
engine = create_engine(config.URL_DB)
Session = sessionmaker(bind=engine)
