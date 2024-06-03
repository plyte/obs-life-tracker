from abc import abstractmethod, ABC


class Repository(ABC):
    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def update(self, id: str, item):
        raise NotImplementedError

    @abstractmethod
    def create(self, id: str, item):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError