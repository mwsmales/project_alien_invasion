import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialise the ship and its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load and resize the ship image, then get its rect (rectangular dimensions)
        self.image = pygame.image.load(ai_settings.ship_image)
        self.image = pygame.transform.smoothscale(self.image, (ai_settings.ship_width, ai_settings.ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom centre of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's centre
        self.center = float(self.rect.centerx)

        # set movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current locations."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag"""
        # firstly update the ship's centre value (not the rect)
        # also prevent ship going off the edge of the screen
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # then update the ship's rect from self.centre
        self.rect.centerx = self.center

    def center_ship(self):
        """Recentre the ship in the middle of the screen"""
        # Stop the ship moving if it was already
        self.moving_right = False
        self.moving_left = False
        #update ship's centre
        self.center = self.screen_rect.centerx
        # update the ship's rect from self.centre
        self.rect.centerx = self.center

