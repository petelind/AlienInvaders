import pygame
from pygame.sprite import Group # fancy list for games

import game_functions as gf
from Ship import Ship
from Alien import Alien
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion!")
    ship = Ship(screen, ai_settings)
    alien = Alien(ai_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()

