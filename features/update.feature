@fixture.Player
Feature:
    As a player I want to update my life total and have that reflected on the other side

    Scenario: I took a point of damage
        When the user ticks down a life point
        Then the lifetotal is updated

    Scenario: I gained life
        When the user ticks up a life point
        Then the lifetotal is updated 

    