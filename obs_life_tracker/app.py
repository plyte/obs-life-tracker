from fastapi import FastAPI
from pydantic import BaseModel
from obs_life_tracker.services.life import Life

app = FastAPI()

db = {
    "1": 20,
    "2": 20,
}

class Direction(BaseModel):
    direction: str

class Total(BaseModel):
    total: int

@app.get("/player/{player_id}/life", response_model=Total)
async def get_players_life_total(player_id: str):
    life_inmemory_repository = LifeInMemoryRepository(db)
    life = Life(life_inmemory_repository)
    total = life.get(player_id)
    return Total(total=total)
