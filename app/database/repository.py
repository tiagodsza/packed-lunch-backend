from app.database.config import Session


class Repository:
    def __init__(self):
        self._db: Session

    def set_db(self, session: Session):
        self._db = session

    def close(self):
        self._db.close()

    def get(self, model):
        response = self._db.query(model).filter(model.deleted_at == None)
        return response.all()

    def get_by_id(self, model, id):
        response = self._db.query(model).get(id)
        return response

    def save(self, model):
        self._db.add(model)
        self._db.commit()


def create_repository():
    try:
        repository = Repository()
        repository.set_db(Session())
        yield repository
    finally:
        repository.close()


def get_repository():
    return next(create_repository())
