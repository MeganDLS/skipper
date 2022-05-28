from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollidePenguinAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ice = cast.get_first_actor(ICE_GROUP)
        penguin = cast.get_first_actor(PENGUIN_GROUP)
        
        penguin_body = penguin.get_body()
        #TODO for each ice in ?
        ice_body = ice.get_body()

        if self._physics_service.has_collided(ice_body, penguin_body):
            penguin.bounce_y()
            sound = Sound(CLINK_SOUND)
            self._audio_service.play_sound(sound)   