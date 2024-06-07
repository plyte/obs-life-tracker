import uuid
from typing import Tuple

from obs_life_tracker.domain.player import Player
from obs_life_tracker.domain.state import State
from obs_life_tracker.view.game_state import CreateGame


class GameDoesNotExist(Exception):
    pass


class StateService:

    def __init__(self, repo):
        self.repo = repo

    def get(self, id: uuid.UUID) -> State:
        response = self.repo.get_by_id(str(id))
        if not response:
            raise GameDoesNotExist(f"Game at id ({id}) does not exist")
        return State(**response)

    def reset(self, id: uuid.UUID) -> State:
        current_state = self.get(id)
        new_player_state = [player.reset() for player in current_state.players]
        new_state = State(
            players=new_player_state,
            ended=False
        )
        response = self.repo.update(str(id), new_state.dict())
        return State(**response)

    def set(self, id: uuid.UUID, state: State):
        response = self.repo.set(str(id), state.json())
        return response

    def create(self, create_game: CreateGame) -> Tuple[State, uuid.UUID]:
        new_player_state = [Player(total=create_game.starting_life_total) for _ in range(create_game.number_of_players)]
        new_id = uuid.uuid4()
        new_state = State(
            players=new_player_state,
            ended=False
        )
        response = self.repo.create(str(new_id), new_state.dict())
        return State(**response), new_id
