import uuid
from typing import List

from pydantic import BaseModel

from obs_life_tracker.domain.player import Player


class GameState(BaseModel):
    id: uuid.UUID
    players: List[Player]
    ended: bool


class CreateGame(BaseModel):
    action: str
    number_of_players: int
    starting_life_total: int
