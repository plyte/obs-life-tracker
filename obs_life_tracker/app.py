from fastapi import FastAPI
from pydantic import BaseModel

from obs_life_tracker.repo.life import LifeInMemoryRepository
from obs_life_tracker.services.life import Life
from obs_life_tracker.view.direction import Direction
from obs_life_tracker.view.total import Total

app = FastAPI()

db = {
    "1": {
        "total": 20,
    },
    "2": {
        "total": 20,
    }
}


@app.get("/player/{player_id}/life", response_model=Total)
async def get_players_life_total(player_id: str):
    life_in_memory_repository = LifeInMemoryRepository(db)
    life = Life(life_in_memory_repository)
    total = life.get(player_id)
    return Total(**total.dict())


@app.patch("/player/{player_id}/life", response_model=Total)
async def get_players_life_total(player_id: str, direction: Direction):
    life_in_memory_repository = LifeInMemoryRepository(db)
    life = Life(life_in_memory_repository)
    total = life.adjust(player_id, in_direction=direction)
    return Total(total=total)
