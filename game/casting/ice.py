import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Ice(Actor):
    """ """
    def __init__(self, body, image, debug = False):
        """
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self.lanes = []
    
    def get_body(self):
        """Gets the body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the image.
        
        Returns:
            An instance of Image.
        """
        return self._image


    #appear
    #TODO move?
    def ice_berg(self):
        for n in range(ICE_QUANTITY):
            vx = random.choice([10, SCREEN_WIDTH])
            vy = random.randint(5, SCREEN_HEIGHT - 400)
            
            # x = random.randint(1, SCREEN_WIDTH - 1)
            # y = random.randing(1, SCREEN_HEIGHT - 1)
        
            self._body.set_velocity
            # position = Point(x, y)
            # position = position.scale(ICE_WIDTH)

    def move_next(self):
        """Moves to the left or just down
        """
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

        # x = (self._position.get_x() + self._velocity.get_x()) % max_x
        # y = (self._position.get_y() + self._velocity.get_y()) % max_y
        # self._position = Point(x, y)


    

    def wrap():
        pass

    def get_points(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points