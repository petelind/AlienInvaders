import pygame


class Ship:
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.image = pygame.image.load('Resources/spaceship.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.speed_factor = ai_settings.speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        :purpose: moves players ship around the screen
        :return: nothing
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += (1 * self.speed_factor)

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= (1 * self.speed_factor)