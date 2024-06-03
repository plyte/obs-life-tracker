from pydantic import BaseModel
from enum import Enum


class DirectionEnum(Enum):
    UP = "up"
    DOWN = "down"


class Direction(BaseModel):
    direction: DirectionEnum