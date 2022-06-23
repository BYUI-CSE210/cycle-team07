"""Global Imports"""
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the other player, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False 

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        scores = cast.get_actors("scores")
        cycles = cast.get_actors("cycles")

        cycle_1 = cycles[0].get_head()
        cycle_2 = cycles[1].get_head()

        cycle_1_segments = cycles[0].get_segments()
        cycle_2_segments = cycles[1].get_segments()

        # Blue is cycle_2 (WASD). This for loop checks if player # 2(Blue) runs into player # 1(Green)'s trail
        for segment in cycle_1_segments:
            if cycle_2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                scores[1].add_points(1)
                fail_reason = "Blue hit Green's trail!"
                winner = "Green"
                result = {"A": fail_reason, "B": winner}
                return result

        # Green is cycle_1 (IJKL). This checks if player # 1(Green) runs into player # 2(Blue)'s trail
        for segment in cycle_2_segments:
            if cycle_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                scores[0].add_points(1)
                fail_reason = "Green hit Blue's trail!"
                winner = "Blue"
                result = {"A": fail_reason, "B": winner}
                return result

        # checks if green hit its own trail
        for segment in cycle_1_segments[1:]:
            if cycle_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                scores[0].add_points(1)
                fail_reason = "Green hit its own trail!"
                winner = "Blue"
                result = {"A": fail_reason, "B": winner}
                return result

        # checks if Blue hit its own trail
        for segment in cycle_2_segments[1:]:
            if cycle_2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                scores[0].add_points(1)
                fail_reason = "Blue hit its own trail!"
                winner = "Green"
                result = {"A": fail_reason, "B": winner}
                return result

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            cycle_1_segments = cycles[0].get_segments()
            cycle_2_segments = cycles[1].get_segments()
            segments = cycle_1_segments + cycle_2_segments

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            winner_position = Point(x, y)
            fail_reason_position = Point(x, (y+20))

            for segment in segments:
                segment.set_color(constants.WHITE)
            for cycle in cycles:
                cycle.set_color(constants.WHITE)
            
            result = self._handle_segment_collision(cast)
            fail_reason = result["A"]
            winner = result["B"]
            fail_reason_message = Actor()
            winner_message = Actor()
            fail_reason_message.set_text(fail_reason)
            fail_reason_message.set_position(fail_reason_position)
            winner_message.set_text(f"Game Over! {winner} is the winner!")
            winner_message.set_position(winner_position)
            cast.add_actor("messages", winner_message)
            cast.add_actor("messages", fail_reason_message)