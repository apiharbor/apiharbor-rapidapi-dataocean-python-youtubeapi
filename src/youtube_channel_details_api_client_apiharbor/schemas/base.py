from pydantic import BaseModel

class BaseModelORM(BaseModel):
    class Config:
        from_attributes = True