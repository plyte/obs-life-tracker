from obs_life_tracker.domain.player import Player
from obs_life_tracker.repo.interface import Repository


class LifeRepository(Repository):

    def __init__(self):
        pass

    def get_all(self):
        pass

    def get_by_id(self, player_id: str):
        pass

    def update(self, id: str, item):
        pass

    def create(self, id: str, item):
        pass
    
    def delete(self, id: str):
        pass


class LifeInMemoryRepository(Repository):
    def __init__(self, data: dict):
        self.data = data

    def get_all(self):
        return self.data

    def get_by_id(self, id: str) -> Player:
        player = self.data[id]
        return Player(**player)

    def update(self, id: str, item: any) -> Player:
        self.data[id] = item
        return Player(**self.data[id])

    def create(self, id: str, item: any) -> Player:
        self.data[id] = item
        return Player(**self.data[id])

    def delete(self, id: str):
        del self.data[id]
        return

        