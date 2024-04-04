import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 800
TILESIZE = 16
#42 by 42 tile size

#Asteroid Sizes
BIG_ASTEROID_SIZE = TILESIZE * 7
MED_ASTEROID_SIZE = TILESIZE * 5
SM_ASTEROID_SIZE = TILESIZE * 3

#target FPS
FPS = 60

#layers
PLAYER_LAYER = 4
ASTEROID_LAYER = 3

#Lives
PLAYER_LIVES = 3

# vulnerability time in ms
DAMAGE_LOOP = 0

# speeds (temporary)
PLAYER_SPEED = 3
ASTEROID_SPEED = 1

#colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# player bullet variables
BULLET_SPEED = 8
BULLET_COLOR = BLACK 
BULLET_SIZE = 5
SPECIAL_BULLET_COLOR = RED
SPECIAL_BULLET_SPEED = 8

# set powerup image final choice
SPAWN_TIMER_POWERUP = 0
SPAWN_DELAY_POWERUP = 60

# initialize Pygame mixer
pygame.mixer.init()

# imports all the music and sound effects
BACKGROUND_MUSIC = pygame.mixer.Sound('Sounds/Background Music.mp3')
ASTEROID_MUSIC = pygame.mixer.Sound('Sounds/Asteroid Destroyed.mp3')
PLAYER_BULLET_MUSIC = pygame.mixer.Sound('Sounds/Player Bullet.mp3')
SHIP_MUSIC = pygame.mixer.Sound('Sounds/Ship Sounds.mp3')
PLAYER_DESTROYED_MUSIC = pygame.mixer.Sound('Sounds/Player Destroyed.mp3')
POWERUP_MUSIC = pygame.mixer.Sound('Sounds/Obtain Powerup.mp3')
BOMB_MUSIC = pygame.mixer.Sound('Sounds/Explosion.mp3')
        
# play music on separate channels
MUSIC_CHANNEL = pygame.mixer.Channel(0)
ASTEROID_CHANNEL = pygame.mixer.Channel(1)
PLAYER_CHANNEL = pygame.mixer.Channel(2)
PLAYER_DESTROYED_CHANNEL = pygame.mixer.Channel(3)
SHIP_CHANNEL = pygame.mixer.Channel(4)
POWERUP_CHANNEL = pygame.mixer.Channel(5)

# set volume, needs continuous testing
pygame.mixer.Channel(0).set_volume(2)
