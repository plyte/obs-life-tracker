from obs_life_tracker.domain.player import Player
from obs_life_tracker.repo.interface import Repository


class InMemoryRepository(Repository):
    def __init__(self, data: dict, table: str):
        self.data = data
        self.table = table

    def get_all(self):
        return self.data

    def get_by_id(self, id: str) -> dict | None:
        if id not in self.data[self.table].keys():
            return None
        return self.data[self.table][id]

    def update(self, id: str, item: any) -> dict:
        self.data[self.table][id] = item
        return self.data[self.table][id]

    def create(self, id: str, item: any) -> dict:
        self.data[self.table][id] = item
        print(self.data[self.table])
        return self.data[self.table][id]

    def delete(self, id: str):
        del self.data[self.table][id]
        return

        