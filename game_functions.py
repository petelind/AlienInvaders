import sys

import pygame

from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """
        Purpose: mediator - iterates over events and reacts by calling appopriate function
        :return: nothing
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()

        # check if key was pressed
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # if player pressed "go left"...
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)


def fire_bullet(ai_settings, bullets, screen, ship):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """
    :Purpose updates objects on the screen
    :param ai_settings: game settings of Settings
    :param screen: game screen of pygame.screen
    :param ship: player ship of Ship
    :return: nothing
    """
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    bullets.update()