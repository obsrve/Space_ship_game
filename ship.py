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

    def blitme(self):
        self.screen.blit(self.image, self.rect)
