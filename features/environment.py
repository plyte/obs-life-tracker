from behave import fixture, use_fixture
from fastapi.testclient import TestClient
from obs_life_tracker.app import app
from obs_life_tracker.fixtures import Player

@fixture
def player(context):
    test_app = TestClient(app)
    context.Player = Player(test_app)
    yield context.Player


def before_tag(context, tag):
    if tag == "fixture.Player":
        use_fixture(player, context)