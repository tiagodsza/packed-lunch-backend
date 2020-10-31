import pyodbc
from sqlalchemy.orm import sessionmaker

import config
from app.database.config import session

connection_string = (
    f'DRIVER={config.DRIVER};'
    f'SERVER={config.SERVER};'
    f'DATABASE={config.DATABASE};'
)

class Repository:
    def __init__(self):
        self._db: session

    def set_db(self, session:session):
        self._db = session

    def close(self):
        self._db.close()

    def get(self, query):
        pass

    def insert(self, model):
        session.add(model)
        session.commit()

def get_repository():
    try:
        repository = Repository()
        repository.set_db(session)
        yield repository
    finally:
        repository.close()