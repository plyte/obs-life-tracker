from obs_life_tracker.fixtures import Player

@when(u'the user ticks down a life point')
def step_impl(context):
    Player = context.Player
    context.previous_life_total = Player.get_life_total("1")
    Player.tick_down("1", times=1)


@then(u'the life total is updated')
def step_impl(context):
    Player = context.Player
    total = Player.get_life_total("1")
    assert total.total != context.previous_life_total


@when(u'the user ticks up a life point')
def step_impl(context):
    Player = context.Player
    context.previous_life_total = Player.get_life_total("1")
    context.Player.tick_up("1", times=1)