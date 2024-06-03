
class LifeRepository(Repository):

    def __init__(self):
        pass

    def get_all(self):
        pass

    def get_by_id(self, player_id: str):
        pass

    def update(self, item):
        pass

    def create(self, item):
        pass
    
    def delete(self, id: str):
        pass


class LifeInMemoryRepository(Repository):
    def __init__(self, data: dict):
        self.data = data

    def get_all(self):
        return data

    def get_by_id(self, id: str):
        return data[id]

    def update(self, item: any):
        return data[item.id] = item

    def create(self, item: any):
        data[item.id] = item
        return data[item.id]

    def delete(self, id: str):
        del data[id]
        return

        