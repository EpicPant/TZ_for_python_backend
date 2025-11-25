from pydantic import BaseModel


class SourceCreate(BaseModel):
    name: str


class SourceResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
