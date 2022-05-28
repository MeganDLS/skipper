"""
"""
from pathlib import Path
from game.casting.color import Color
from game.casting.image import Image

#Set up an absolute pathto see what the parent directory is
ROOTDIR = Path(__file__).parent
#Calling the div operator to concatenate - works on linux mac and windows.
ASSETSDIR = ROOTDIR / "assets"
FONTS = ROOTDIR / ASSETSDIR / "fonts"
IMAGES = ROOTDIR / ASSETSDIR / "images"
SOUNDS = ROOTDIR / ASSETSDIR / "sounds"
# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Skipper"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_SERIF = ASSETSDIR / FONTS / "Quicksand-Medium.ttf"
FONT_SMALL = 25
FONT_LARGE = 50

# SOUND
CLINK_SOUND = ASSETSDIR / SOUNDS / "ice.wav"
WELCOME_SOUND = ASSETSDIR / SOUNDS / "splash.wav"
OVER_SOUND = ASSETSDIR / SOUNDS / "bubbles.wav"
MUSIC = ASSETSDIR / SOUNDS / "happyfeet.mp3"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(109, 104, 117)
ICE = Color(219, 241, 253)
PEACH = Color(255, 180, 162)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
SCENE_NEW_GAME = 0
SCENE_TRY_AGAIN = 1
SCENE_NEXT_LEVEL = 2
SCENE_IN_PLAY = 3
SCENE_GAME_OVER = 4

#### TODO
# # LEVELS
LEVEL_FILE = ASSETSDIR / "data" / "level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

#STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15

SCORE_GROUP = "score"
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
# LEVEL_FORMAT = "Skipper"

#TODO switch out penguin with each life or level
LEVEL_FORMAT = "Scene: {}"
LIVES_FORMAT = "Lives: {}"
SCORE_FORMAT = "Cheezy Dibbles: {}"

# ICE CUBES
ICE_GROUP = "ice"
ICE_IMAGE = Image(ASSETSDIR / IMAGES / "smlice.png")
ICE_WIDTH = 200
ICE_HEIGHT = 488
ICE_VELOCITY = 4
ICE_QUANTITY = 5

# JUMPER PENGUIN
PENGUIN_GROUP = "penguins"
PENGUIN_IMAGES = Image(ASSETSDIR /"images" / "smlskipper.png")

# PENGUIN_IMAGES = ASSETSDIR / IMAGES / "smlskipper.png"
PENGUIN_WIDTH = 132
PENGUIN_HEIGHT = 136
PENGUIN_VELOCITY = 5
PENGUIN_RATE = 6


# TODO if theres time.
# CHEEZY DIBBLES
DIBBLE_GROUP = "dibbles"
DIBBLE_IMAGE = ASSETSDIR / IMAGES / "cheeto.png"
DIBBLE_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "Welcome to Skipper! ~ PRESS ENTER TO START"
PREP_TO_LAUNCH = "GET READY TO PLAY"
WAS_GOOD_GAME = "GAME OVER"