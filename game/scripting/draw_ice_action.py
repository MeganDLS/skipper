"""
"""
from constants import *
from game.scripting.action import Action


class DrawIceAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ice = cast.get_actors(ICE_GROUP)
        
        for i in ice:
            body = ice.get_body()

            if ice.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, BLACK)
                
            animation = ice.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)