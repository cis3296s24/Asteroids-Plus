import pygame
from AsteroidsRound import *
from button import *
from config import *


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.running = True
        self.playButton = Button((5, 5), (100, 100), (0,255,0), "PLAY")
        self.exitButton = Button((215, 5), (100, 100), (0,255,0), "EXIT")
        
        
    def draw(self):
        self.screen.fill(WHITE)
        pygame.mouse.set_visible(True)
        
        self.playButton.draw(self.screen)
        self.exitButton.draw(self.screen)
    
        pygame.display.update()
        
    def play(self):
        while True:
            m.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

                if self.playButton.is_clicked(event):
                        g = Game() #init Game class
                        g.new() #create a new game everytime we run
                        while g.running:
                            g.main()
                        break

                if self.exitButton.is_clicked(event):
                    # exit
                    pygame.quit()
                    exit()
        
m = Menu()
while m.running:
    m.play()
