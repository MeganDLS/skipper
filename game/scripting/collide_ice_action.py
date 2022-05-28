from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideIceAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        penguin = cast.get_first_actor(PENGUIN_GROUP)
        ice = cast.get_actors(ICE_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for i in ice:
            penguin_body = penguin.get_body()
            ice_body = ice.get_body()

            if self._physics_service.has_collided(penguin_body, ice_body):
                penguin.bounce_y()
                sound = Sound(CLINK_SOUND)
                self._audio_service.play_sound(sound)
                points = ice.get_points()
                stats.add_points(points)
                cast.remove_actor(ICE_GROUP, ice)