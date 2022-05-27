"""
"""
from constants import *
from game.scripting.action import Action


class DrawPenguinAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        penguin = cast.get_first_actor(PENGUIN_GROUP)
        body = penguin.get_body()

        if penguin.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        # animation = penguin.get_animation()
        # image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(PENGUIN_IMAGES, position)