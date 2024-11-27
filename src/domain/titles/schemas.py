from pydantic import BaseModel


class TitlesSchema(BaseModel):
    id: int
    title: str


class CreateTitleSchema(BaseModel):
    title: str
