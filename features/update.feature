@fixture.Player
Feature:
    As a player I want to update my life total and have that reflected on the other side

    Scenario: I took a point of damage
        When the user ticks down a life point
        Then the life total is updated

    Scenario: I gained life
        When the user ticks up a life point
        Then the life total is updated

    Scenario: The players reset life totals
        Given a game exists
        When the users want to reset the life totals
        Then the life totals are set back to the default values
