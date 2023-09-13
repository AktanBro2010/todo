from pydantic import BaseModel


class CreateToDO(BaseModel):
    task: str


class ToDo(BaseModel):
    id: int
    task: str

    class Config:
        from_attributes = True