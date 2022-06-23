import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points.
    """
    def __init__(self, position = 1):
        super().__init__()
        self._segments = []

        self.position = position
        self.color = constants.GREEN

        self._prepare_body()

    def get_segments(self):

        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):

        return self._segments[0]

    def leave_trail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self.color)
            self._segments.append(segment)

    def turn_head(self, velocity):

        self._segments[0].set_velocity(velocity)
    


    def _prepare_body(self):

        if self.position == 1:
            x = int((constants.MAX_X * constants.CELL_SIZE) / 4)
            color = self.color
        else:
            x = int((constants.MAX_X * constants.CELL_SIZE) - ((constants.MAX_X * constants.CELL_SIZE)/ 4))
            self.color = constants.BLUE
            color = self.color

        y = int(constants.MAX_Y / 3)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x , y + i * constants.CELL_SIZE)
            velocity = Point(0, -constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def set_color(self,color):

        self.color = color