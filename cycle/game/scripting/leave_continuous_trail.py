from game.scripting.action import Action

class LeaveTrail(Action):
    """
    An update action that leaves a trail coming from the growing snake.
    
    The responsibility of Make trail action is to increase the trial of the players
    """
    def execute(self, cast, script):
        """Executes the Make trail action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
            
        """
        snakes = cast.get_actors("snakes")
        for snake in snakes:
            snake.leave_trail(1)
