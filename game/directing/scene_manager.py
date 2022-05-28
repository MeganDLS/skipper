"""
"""
import csv
from constants import *
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.stats import Stats
from game.casting.text import Text 
from game.casting.dibbles import Dibbles
from game.casting.ice import Ice
from game.casting.penguin import Penguin
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_penguin_action import CollidePenguinAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_ice_action import CollideIceAction
from game.scripting.control_penguin_action import ControlPenguinAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_penguin_action import DrawPenguinAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_ice_action import DrawIceAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ice_action import MoveIceAction
from game.scripting.move_penguin_action import MovePenguinAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_PENGUIN_ACTION = CollidePenguinAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_ICE_ACTION = CollideIceAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_PENGUIN_ACTION = ControlPenguinAction(KEYBOARD_SERVICE)
    DRAW_ICE_ACTION = DrawIceAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_PENGUIN_ACTION= DrawPenguinAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_PENGUIN_ACTION = MovePenguinAction()
    MOVE_ICE_ACTION = MoveIceAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)


    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
            #TODO Add another level? prepare_next_level TRY_AGAIN
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_ice(cast)
        self._add_penguin(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):
        self._add_ice(cast)
        self._add_penguin(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, MUSIC))

    def _prepare_try_again(self, cast, script):
        self._add_penguin(cast)
        #TODO try self._add_ice(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_penguin(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_PENGUIN_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_penguin(cast)
        #TODO try self._add_ice(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_penguin(self, cast):
        penguin = cast.get_first_actor(PENGUIN_GROUP)
        # penguin.move_next()

    def _add_ice(self, cast):
        cast.clear_actors(ICE_GROUP)

        stats = cast.get_first_actor(STATS_GROUP)

        # x = SCREEN_WIDTH / 3
        # y = CENTER_Y / 5
        # position = Point(x, y)
        # size = Point(ICE_WIDTH, ICE_HEIGHT)
        # #TODO Not velocity?
        # velocity = Point(0, 0)
        # body = Body()
        # image = Image(ICE_IMAGE)
        # #TODO animation
        # ice = Ice(body, image, True)
        # cast.add_actor(ICE_GROUP, ice)

    def _add_penguin(self, cast):
        cast.clear_actors(PENGUIN_GROUP)
        x = CENTER_X - PENGUIN_WIDTH / 2
        y = SCREEN_HEIGHT - PENGUIN_HEIGHT
        position = Point(x, y)
        size = Point(PENGUIN_WIDTH, PENGUIN_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(PENGUIN_IMAGES, PENGUIN_RATE)
        penguin = Penguin(body, image)
        cast.add_actor(PENGUIN_GROUP, penguin)

    def _activate_ice(self, cast):
        ice = cast.get_first_actor(ICE_GROUP)
        ice.move_next()

    # def _add_ice(self, cast):
    #     cast.clear_actors(ICE_GROUP)
    #     stats = cast.get_first_actor(STATS_GROUP)
    #     x = FIELD_RIGHT - ICE_WIDTH
    #     y = FIELD_TOP - 200
    #     position = Point(x, y)
    #     size = Point(ICE_WIDTH, ICE_HEIGHT)
    #     velocity = Point(0, 0)
    #     body = Body(position, size, velocity)
    #     image = Image(ICE_IMAGE)
    #     ice = Ice(position, size, velocity)
    #     cast.add_actor(ICE_GROUP, ice)
        
    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_SERIF, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_SERIF, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_SERIF, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)
    
    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_SERIF, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_ICE_ACTION)
        script.add_action(OUTPUT, self.DRAW_PENGUIN_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_ICE_ACTION)
        script.add_action(UPDATE, self.MOVE_PENGUIN_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_ICE_ACTION)
        script.add_action(UPDATE, self.COLLIDE_PENGUIN_ACTION)
        #TODO move again
        script.add_action(UPDATE, self.MOVE_PENGUIN_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)

   