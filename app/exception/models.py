from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND


class NotFoundException(HTTPException):
    def __init__(self, message: str = 'Not found!'):
        super().__init__(status_code=HTTP_404_NOT_FOUND)
        self.detail = message
