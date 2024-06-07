import uuid
from typing import List

from pydantic import BaseModel

from obs_life_tracker.domain.player import Player


class State(BaseModel):
    players: List[Player]
    ended: bool