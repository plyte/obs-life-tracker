from pydantic import BaseModel


class Player(BaseModel):
    total: int = 20

    @staticmethod
    def reset() -> "Player":
        return Player()
