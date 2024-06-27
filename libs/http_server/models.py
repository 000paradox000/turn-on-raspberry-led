from pydantic import BaseModel


class InputMessage(BaseModel):
    state: bool


class OutputMessage(BaseModel):
    state: bool
    modified: bool


class InputTextMessage(BaseModel):
    value: str


class OutputTextMessage(OutputMessage):
    value: str
