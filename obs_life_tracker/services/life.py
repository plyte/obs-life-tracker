from obs_life_tracker.domain.player import Player
from obs_life_tracker.repo.interface import Repository
from obs_life_tracker.view.direction import Direction, DirectionEnum


class UserDoesNotExist(Exception):
    pass


class Life:

    def __init__(self, life_repository: Repository):
        self.life_repository = life_repository

    def adjust(self, player_id: str, in_direction: Direction):
        player = self.life_repository.get_by_id(player_id)
        if player is None:
            raise UserDoesNotExist()
        if in_direction.direction == DirectionEnum.UP:
            self.life_repository.update(player_id, {"total": player.total + 1})
            return player.total + 1
        if in_direction.direction == DirectionEnum.DOWN:
            self.life_repository.update(player_id, {"total": player.total - 1})
            return player.total - 1

    def get(self, player_id: str) -> Player:
        total = self.life_repository.get_by_id(player_id)
        if total is None:
            raise UserDoesNotExist()
        return total

    def update(self, player_id: str, to: int):
        pass
