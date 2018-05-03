import pygame

from common.settings import Settings

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
pygame.display.set_caption(Settings.project_name)
crashed = False


class ImagesDrawer(object):
    def __init__(self, images):
        self.images = images

    def draw(self, time):
        game_display.fill(Settings.background_color)

        for image in self.images:
            image.draw(time)
        pygame.display.update()


def window_closed():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def image(name):
    return Settings.images_path + name
