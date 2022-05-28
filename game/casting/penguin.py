"""
"""
import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Penguin(Actor):
    """ """
    def __init__(self, body, image, debug = False):
        """
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def bounce_x(self):
        """Bounces the ball in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the ball in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_image(self):
        """Gets the image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves forward
        """
        
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the bat to the left."""
        velocity = Point(-PENGUIN_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the bat to the right."""
        velocity = Point(PENGUIN_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def swing_up(self):
        velocity = Point(0, PENGUIN_VELOCITY)
        self._body.set_velocity(velocity)

    #TODO jump over ice

    # def release(self):
    #     """Release the ball in a random direction."""
    #     # rn = random.uniform(0.9, 1.1)
    #     # vx = random.choice([-PENGUIN_VELOCITY * rn, PENGUIN_VELOCITY * rn])
    #     # vy = -PENGUIN_VELOCITY
    #     velocity = Point(vx, vy)
    #     self._body.set_velocity(velocity)

    def jump(self):
        """
        """
        pass

    def stop_moving(self):
        """Stops moving
        """
        velocity = Point(0,0)
        self._body.set_velocity(velocity)