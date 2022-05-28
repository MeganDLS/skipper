"""
"""
from constants import *
from game.casting.point import Point
from game.scripting.action import Action

class MoveIceAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        ice = cast.get_actors(ICE_GROUP)
        for i in ice:
            body = i.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            x = position.get_x()

            position = position.add(velocity)

            if x < 0 :
                position = Point(x, position.get_y())
            elif x > (SCREEN_WIDTH - ICE_WIDTH):
                position = Point(SCREEN_WIDTH - ICE_WIDTH, position.get_y())

            body.set_position(position)

