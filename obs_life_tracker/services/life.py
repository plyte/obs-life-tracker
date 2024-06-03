from obs_life_tracker.repo.interface import Repsitory

class Life:

    def __init__(self, life_repository: Repository):
        self.life_repository = life_repository
    
    def increment(self, player_id: str):
        pass

    def decrement(self, player_id: str):
        pass

    def get(self, player_id: str):
        total = self.life_repository.get_by_id(player_id)
        return total

    def update(self, player_id: str, to: int):
        pass