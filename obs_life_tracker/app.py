import uuid

from fastapi import FastAPI
from pydantic import BaseModel

from obs_life_tracker.repo.in_memory import InMemoryRepository
from obs_life_tracker.services.life import Life
from obs_life_tracker.services.state import State, StateService
from obs_life_tracker.view.direction import Direction
from obs_life_tracker.view.game_state import GameState, CreateGame
from obs_life_tracker.view.total import Total

app = FastAPI()

db = {
    "players": {
        "1": {
            "total": 20,
        },
        "2": {
            "total": 20,
        }
    },
    "games": {},
}


@app.get("/player/{player_id}/life", response_model=Total)
async def get_players_life_total(player_id: str):
    life_in_memory_repository = InMemoryRepository(db, "players")
    life = Life(life_in_memory_repository)
    total = life.get(player_id)
    return Total(**total.dict())


@app.patch("/player/{player_id}/life", response_model=Total)
async def get_players_life_total(player_id: str, direction: Direction):
    life_in_memory_repository = InMemoryRepository(db, "players")
    life = Life(life_in_memory_repository)
    total = life.adjust(player_id, in_direction=direction)
    return Total(total=total)


@app.post("/game/{id}", response_model=GameState)
async def modify_game_state(id: uuid.UUID):
    print(id)
    state_repository = InMemoryRepository(db, "games")
    state = StateService(state_repository)
    current_state = state.reset(id)
    return GameState(id=id, **current_state.dict())


@app.post("/game", response_model=GameState)
async def make_game(create_game: CreateGame):
    state_repository = InMemoryRepository(db, "games")
    state = StateService(state_repository)
    new_game_state, id = state.create(create_game)
    return GameState(id=id, **new_game_state.dict())
