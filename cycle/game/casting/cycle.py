"""Global Imports"""
import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point

class Cycle(Actor):
    """
    A cycle that leaves a trail behind itself to hit the other player with
    
    The responsibility of Cycle is to move itself.

    Attributes:
        super().__init__(): The attributes inherited from the parent class "Actor"
        _segments (list): empty list that is later filled with the amount of segments for the cycle
        position: (string): position of the cycle
        color: (string): color of the cycle
    """
    def __init__(self, position = 1):
        super().__init__()
        self._segments = []
        self.position = position
        self.color = constants.GREEN
        self._prepare_body()

    def get_segments(self):
        """Get the current number of cycle segments"""
        return self._segments

    def move_next(self):
        """Move the next segment in the cycle
        
        Args:
            segment (string): The individual pieces of the "self._segments" list
            i (int): counts the length of the "self._segments" list and updates the velocity of each segment
        """
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
        """Gets the head of the cycle
        
        Args:
            self._segments[0] (int index): the first index of the _segments list which is the head of the cycle
        """
        return self._segments[0]

    def leave_trail(self, number_of_segments):
        """Slowly increase the length of the cycle's trail
        
        Args:
            tail (int): the length of the cycle's trail
            velocity (int): the velocity of the cycle
            position (int): The position of the cycle
            segment: individual pieces of the cycle // instance of the Actor class
            segment_add_chance (randint): 1 in 5 chance to lengthen the cycle's trail to balance the difficulty of the game
        """
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
            # these next few lines get a random number and has a 1 in 5 chance to append another segment to each cycle to slowly increase the length of the cycles. 1 in 5 is the best balance I found so far
            segment_add_chance = random.randint(0, 5)
            if segment_add_chance == 5:
                self._segments.append(segment)

    def turn_head(self, velocity):
        """Turn the head of the cycle at the normal velocity in a 90 degree angle"""
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """Creates the entire base cycle at a set length
        
        Args:
            velocity (int): the velocity of the cycle
            position (int): The position of the cycle
            text (string): The text of the cycle
            segment: individual pieces of the cycle // instance of the Actor class
        """

        if self.position == 1:
            x = int((constants.MAX_X * constants.CELL_SIZE) / 4)
            color = self.color
        else:
            x = int((constants.MAX_X * constants.CELL_SIZE) - ((constants.MAX_X * constants.CELL_SIZE)/ 4))
            self.color = constants.BLUE
            color = self.color

        y = int(constants.MAX_Y / 3)

        for i in range(constants.CYCLE_LENGTH):
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
        """Set the color of the cycle
        
        Args:
            color (string): The color of the cycle
        """
        self.color = color