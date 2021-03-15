import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """initialise the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/alien1.png')
        self.image = pygame.transform.smoothscale(self.image, (ai_settings.alien_width, ai_settings.alien_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # start each new alien near the top left of the screen (one image width / height from screen edge length)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the alien position"""
        # firstly update the alien's centre value (not the rect)
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        # then update the alien's rect
        self.rect.x = self.x

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= self.screen_rect.left:
            return True