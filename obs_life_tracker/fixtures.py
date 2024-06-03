from fastapi.testclient import TestClient

from obs_life_tracker.view.total import Total


class Player:

    def __init__(self, client: TestClient):
        self.client = client

    def tick_down(self, player_id: str, times=1) -> Total:
        decrement_life = {
            "direction": "down"
        }
        response = self.client.patch(f"/player/{player_id}/life",
            json=decrement_life
        )
        assert response.status_code == 200
        return Total(**response.json())

    def tick_up(self, player_id: str, times=1) -> Total:
        increment_life = {
            "direction": "up"
        }
        response = self.client.patch(f"/player/{player_id}/life",
            json=increment_life
        )
        assert response.status_code == 200
        return Total(**response.json())

    def get_life_total(self, player_id: str) -> Total:
        response = self.client.get(f"/player/{player_id}/life")
        assert response.status_code == 200
        return Total(**response.json())