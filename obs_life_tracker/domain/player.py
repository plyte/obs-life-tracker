from pydantic import BaseModel


class Player(BaseModel):
    total: int