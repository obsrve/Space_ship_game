import pygame


class Ship():

    def __init__(self, ai_game):
        """Initialization of the ship and his start position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Download image and his rect
        self.image = pygame.image.load('alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()

        # Create every new ship in bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement indicators
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update position of the ship base on movemet indicators
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
