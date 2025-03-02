import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    #Overall class to manage game assets and behavior 

    def __init__(self):
        #Initialize the game, and create game resources
        self.settings = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        #Start the main loop of the game

        #Watch for keyboard and mouse events
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
    #Update position of bullets and get rid of old bullets
    #Update bullet positions
        self.bullets.update()
        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))



    def _update_screen(self):
        #Make the most recently drawn screen visible
        self.screen.fill(self.settings.backgroundColor)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Redraw the screen during each pass through the loop
        pygame.display.flip()
    
    
    def _check_events(self):
        #Respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    
    def _check_keydown_events(self, event):
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
            elif event.key == pygame.K_q:
                sys.exit()
    
    def _check_keyup_events(self, event):
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.ship.moving_left = False


    def _fire_bullet(self):
        #Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()