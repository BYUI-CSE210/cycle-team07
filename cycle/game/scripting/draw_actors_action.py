"""Global Imports"""
import constants
from game.scripting.action import Action
from game.shared.point import Point


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycles = cast.get_actors("cycles")
        scores = cast.get_actors("scores")
        messages = cast.get_actors("messages")
        scores[1].set_position(Point(constants.MAX_X - (constants.CELL_SIZE * 15), 0))

        self._video_service.clear_buffer()
        for cycle in cycles:
            cycle_segments = cycle.get_segments()
            self._video_service.draw_actor(cycle)
            self._video_service.draw_actors(cycle_segments)
        for score in scores:
            self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)

        self._video_service.flush_buffer()

        cycles = cast.get_actors("cycles2")
        self._video_service.clear_buffer()
        for cycle in cycles:
            segments = cycle.get_segments()
            self._video_service.draw_actors(segments)
            
        messages = cast.get_actors("messages")