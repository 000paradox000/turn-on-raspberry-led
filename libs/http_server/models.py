from pydantic import BaseModel


class InputMessage(BaseModel):
    state: bool


class OutputMessage(BaseModel):
    state: bool
    modified: bool
