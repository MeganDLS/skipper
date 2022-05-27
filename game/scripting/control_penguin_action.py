#TODO maybe cheesy dibbles.

from constants import *
# from game.casting.ball import Ball
from game.scripting.action import Action


class ControlPenguinAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        penguin = cast.get_first_actor(PENGUIN_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            penguin.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            penguin.swing_right()  
            #TODO up and down?
        # elif self._keyboard_service.is_key_down(UP): 
        #     racket.swing_up()  
        # elif self._keyboard_service.is_key_down(DOWN): 
        #     racket.swing_down()  
        else: 
            penguin.stop_moving()        