import pygame
from pygame.sprite import _Group, Sprite


class Bullet(Sprite):
    """Class for bullet control"""

    def __init__(self, ai_game):
        """Create object bullet in ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create rect of bullet in (0, 0) and set the correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # save bullet position as decimal value
        self.y = float(self.rect.y)
