import pygame

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Define a class for button objects"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Initialise button properties
        self.height = 50
        self.width = 500
        #set button colour
        self.button_color = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 32)

        #build the button's rect object and centre it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self.msg_prep(msg)

    def msg_prep(self, msg):
        """Turn msg into a rendered image and centre text on the button"""

        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        #set text image centre to that of the button
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)