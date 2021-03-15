class Settings():
    """A class to store the settings for the Alien Invasion game"""

    def __init__(self):
        """initialise the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.screen_colour = (230, 230, 230)
        self.window_x = 80
        self.window_y = 30

        # ship settings
        self.ship_limit = 3
        self.ship_height = 80
        self.ship_width = 50
        self.ship_image = "Images/Ship2.png"

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.alien_height = 52
        self.alien_width = 30

        # Alien fleet settings
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = -1

        # How quickly game speeds up at each level
        self.speed_up_scale = 1.1
        # How quickly the alien point values increase at each level
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        self.alien_speed_factor = 0.5
        self.bullet_speed_factor = 1.5
        self.ship_speed_factor = 0.75

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speeed settings and alien point values"""
        self.alien_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.ship_speed_factor *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)
