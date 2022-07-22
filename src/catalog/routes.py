from pydantic import BaseModel, Field

from fastapi import Cookie, Header, status, HTTPException, Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv


router = InferringRouter()


@cbv(router)
class BooksView:
    pass