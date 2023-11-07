import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Common class which control the resources and behavior of the game"""

    def __init__(self):
        """Initialization of the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Begin main cycle"""
        while True:
            # watch  for event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Install new screen on each copy
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # show last screen
            pygame.display.flip()


if __name__ == '__main__':
    """Create cope of the game and start the game"""
    ai = AlienInvasion()
    ai.run_game()
