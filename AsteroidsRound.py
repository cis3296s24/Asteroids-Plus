import pygame
from sprites import *
import config
from ship import *
from asteroid import *
import sys
from powerups import *

class Game:
    # set the timer for ship spawn
    game_timer = 0
    spawn_timer_ship = 0
    spawn_timer_reg_bullet = 0
    spawn_timer_sp_bullet = 0
    spawn_delay_ship = 20
    spawn_delay_reg_bullet = 20
    spawn_delay_sp_bullet = 60
    ship_exist = False

    asteroid_timer = 0
    asteroid_spawn_delay = 5
    lives = 3

    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Galaxus-z8Mow.ttf', 32)
        self.running = True

        #init sprite sheets
        self.ship_sp_bullets = pygame.sprite.Group()
        self.ship_reg_bullets = pygame.sprite.Group()
        self.ships = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        self.player_bullets = pygame.sprite.Group()

    def new(self):
        
        #new game
        self.playing = True
        
        #take all sprites and bunch them together so we can update all at once if needed
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()

        #create player at middle of screen
        self.player = Player(self, (WIN_WIDTH/TILESIZE)/2, (WIN_HEIGHT/TILESIZE)/2)
    
    def events(self):
        for event in pygame.event.get():
            #when you x-out of window, game quits
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #game loop updates
        self.all_sprites.update()

        self.spawn_timer_ship += 1
        self.spawn_timer_sp_bullet += 1
        self.spawn_timer_reg_bullet += 1
        self.game_timer += 1
        self.asteroid_timer += 1
        config.SPAWN_TIMER_POWERUP += 1
        
        self.asteroid_alg()

        #update direction for special bullet
        for bullet in self.ship_sp_bullets:
            bullet.update_dir(self.player)
            self.spawn_sp_bullet = 0

        # move the ship
        for ship in self.ships:
            ship.move()

        # check if player obtained the powerup
        for powerup in self.powerups:
            powerup.update()

        # create the ship based on time interval
        if self.spawn_timer_ship >= self.spawn_delay_ship * FPS:
            self.spawn_timer_ship = 0
            self.spawn_ship()
            self.ship_exist = True #if destroyed, changes to false
        
        # start shooting for special bullet
        if self.ship_exist and self.spawn_timer_sp_bullet >= self.spawn_delay_sp_bullet * FPS:
            for ship in self.ships:
                ship.shoot_sp_bullet()
            self.spawn_timer_sp_bullet = 0
        
        # start shooting for regular bullet
        if self.ship_exist and self.spawn_timer_reg_bullet >= self.spawn_delay_reg_bullet * FPS:
            for ship in self.ships:
                ship.shoot_reg_bullet()
            self.spawn_timer_reg_bullet = 0

        # increase difficulty - every one minute increase difficulty and both ship and bullet time of spawn decrease by 5
        if self.game_timer >= 60 and self.spawn_delay_sp_bullet > 30:
            #add a screen display of difficult level currently - to do
            if self.spawn_delay_ship > 25:
                self.spawn_delay_ship -= 5
                self.spawn_delay_reg_bullet -= 5
            self.spawn_delay_sp_bullet -= 5
            self.game_timer = 0
        
        # spawn powerups based off the game time
        if config.SPAWN_TIMER_POWERUP >= config.SPAWN_DELAY_POWERUP * FPS:
            powerup = Powerups(self.all_sprites, self.player)
            self.all_sprites.add(powerup)
            self.powerups.add(powerup)
            config.SPAWN_TIMER_POWERUP = 0
        
    #create background screen for game
    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen) #
        self.clock.tick(FPS) #update the screen based on FPS

        lives_text = self.font.render('Lives: ' + str(self.player.lives), False, BLACK)
        
        # Draw the lives text
        self.screen.blit(lives_text, (10, 10))
        pygame.display.update()

    def spawn_ship(self):
        # Create a new ship and add it to the groups
        ship = Ships(self.all_sprites, self.ship_sp_bullets, self.ship_reg_bullets)
        self.all_sprites.add(ship)
        self.ships.add(ship)
        
    def spawn_asteroid(self, size):
        asteroid = Asteroid( self, 0, 0, size)
        self.all_sprites.add(asteroid)
        self.asteroids.add(asteroid)
        

    def asteroid_alg(self):
        size = random.choice([BIG_ASTEROID_SIZE, MED_ASTEROID_SIZE, SM_ASTEROID_SIZE])

        if self.game_timer >= 30:
            self.asteroid_spawn_delay = 4
        if self.game_timer >= 60:
            self.asteroid_spawn_delay = 3

        if self.asteroid_timer >= self.asteroid_spawn_delay * FPS:
            self.spawn_asteroid(size)
            self.asteroid_timer = 0  # Reset the timer after spawning an asteroid

    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

        self.running = False
