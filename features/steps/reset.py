import uuid


@given(u'a game exists')
def step_impl(context):
    new_state_info = context.Player.start_a_game(number_of_players=2, starting_life_totals=20)
    context.game_id = new_state_info.id


@when(u'the users want to reset the life totals')
def step_impl(context):
    context.Player.tick_down("1")
    context.previous_life_total = context.Player.get_life_total("1")
    context.Player.reset_life_total(context.game_id)


@then(u'the life totals are set back to the default values')
def step_impl(context):
    current_value = context.Player.get_life_total("1")
    assert current_value == context.previous_life_total