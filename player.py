import enum
import functools
import string

from construct import (
    Enum, Byte
)

from jj2.protocols.gameplay import Character

@functools.partial(Enum, Byte)
class Flag(enum.IntEnum):
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

@functools.partial(Enum, Byte)
class Team(enum.IntEnum):
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

@functools.partial(Enum, Byte)
class ConnectionType(enum.IntEnum):
    CONNECTING = 0
    CONNECTED = 1
    CTO = 2
    DOWNLOADING = 3

@functools.partial(Enum, Byte)
class Flight(enum.IntEnum):
    NONE = 0
    FLYCARROT = 1
    AIRBOARD = 2

@functools.partial(Enum, Byte)
class Gem(enum.IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2
    PURPLE = 3

@functools.partial(Enum, Byte)
class Light(enum.IntEnum):
    NONE = 0
    NORMAL = 1
    POINT = 2
    POINT2 = 3
    FLICK = 3
    BRIGHT = 4
    LASERBEAM = 5
    LASER = 6
    RING = 7
    RING2 = 8
    PLAYER = 9

class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return str(self.x) + ", " + str(self.y)

class Fur():
    def __init__(self, r, g, b, alpha):
        self.r = r
        self.g = g
        self.b = b
        self.alpha = alpha

class Player():
    def __init__(self, name: string, team: Team, spectating: bool, socketId: int, fur: Fur, character: Character):
        self.name = name
        self.team = team
        self.spectating = spectating
        self.socketId = socketId
        self.fur = fur
        self.coins = 0
        self.curAnim = 0
        self.curFrame = 0
        self.currWeapon = 0
        self.direction = 1 # 1 or -1
        self.doubleJumpCount = 0
        
        if character == Character.SPAZ:
            self.doubleJumpCount = 1
        
        self.fastFire = 35
        self.fly = Flight.NONE
        self.food = 0
        self.frameID = 0
        self.frozen = 0
        self.gems = []
        self.helicopter = 0
        self.helicopterElapsed = 0
        self.idle = 0
        self.jumpStrength = -10
        self.laps = 0
        self.lapTimeBest = 0
        self.lapTimeBest = 0
        self.lapTimes = [] # 5 length
        self.light = 0
        self.lightType = Light.PLAYER
        self.lives = 0
        self.lrsLives = 0
        self.noclipMode = False
        self.noFire = False
        self.platform = 0
        self.playerID = socketId
        self.powerup = [False, False, False, False, False, False, False, False, False]
        self.setID = 0
        self.health = 0
        self.ammo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.score = 0
        self.kills = 0
        self.deaths = 0
        self.ping = 0
        self.position = Vector2(0, 0)
        self.connection = ConnectionType.CONNECTING
        self.flag = Flag.NONE
        self.character = character
