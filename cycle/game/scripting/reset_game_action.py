"""Global Imports"""
from game.scripting.action import Action

class ResetGameAction(Action):
    """This resets the game."""

    def execute(self, cast, script):
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        cast.remove_actor("cycle_one", cycle_one)
        cast.remove_actor("cycle_two", cycle_two)
    