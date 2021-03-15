import os
import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialise pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (ai_settings.window_x, ai_settings.window_y)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a start button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, and group to store aliens and bullets in
    ship = Ship(ai_settings, screen)
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # create the fleet of aliens.
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        game_functions.check_events(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens)

        if stats.game_active == True:
            # update the ship and bullets' positions depending on keystrokes.
            ship.update()
            game_functions.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            game_functions.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            # Redraw the screen during every pass through the game loop.

        game_functions.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
