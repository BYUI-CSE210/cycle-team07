"""Global Imports"""
from game.scripting.action import Action

class LeaveTrail(Action):
    """
    An update action that leaves a growing trail coming from the cycle.
    
    The responsibility of Make trail action is to increase the trial of the players
    """
    def execute(self, cast, script):
        """Executes the Make trail action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
            
        """
        cycles = cast.get_actors("cycles")
        for cycle in cycles:
            cycle.leave_trail(1)
