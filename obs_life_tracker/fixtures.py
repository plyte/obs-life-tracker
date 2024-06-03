from fastapi.testclient import TestClient

class Player:

    def __init__(self, client: TestClient):
        self.client = client

    def tick_down(self, player_id: str, times=1) -> None:
        decrement_life = {
            "direction": "down"
        }
        response = self.client.patch(f"/player/{player_id}/life",
            json=decrement_life
        )
        assert response.status_code == 200
        assert response.json() == {
            "direction": "down"
        }

    def tick_up(self, player_id: str, times=1) -> None:
        increment_life = {
            "direction": "up"
        }
        response = self.client.patch(f"/player/{player_id}/life",
            json=increment_life
        )
        assert response.status_code == 200
        assert response.json() == {
            "direction": "up"
        }

    def get_life_total(self, player_id: str) -> int:
        response = self.client.get(f"/player/{player_id}/life")
        assert response.status_code == 200