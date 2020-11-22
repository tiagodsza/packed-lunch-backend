from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

Base = declarative_base()
parameters = (
    f'DRIVER={config.DRIVER};'
    f'SERVER={config.SERVER};'
    f'DATABASE={config.DATABASE};'
    f'UID={config.DB_USER};'
    f'PWD={config.DB_PASSWORD};'
)
url_parameters_db = quote_plus(parameters)
URL_DB = f'mssql+pyodbc:///?odbc_connect=%s' % url_parameters_db
engine = create_engine(URL_DB)
Session = sessionmaker(bind=engine)
