import pygame
from settings import Settings

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
pygame.display.set_caption(Settings.project_name)
crashed = False


class ImagesDrawer:
    def __init__(self, images):
        self.images = images

    # Draw image if given time is inside duration window.
    def draw(self, time):
        game_display.fill(BACKGROUND_COLOR)

        for image in self.images:
            image.draw(time)
        pygame.display.update()


class ImageDisplay:
    displayed = False

    def __init__(self, image_path, time, duration, pos_x=0, pos_y=0):
        self.image = pygame.image.load(image_path)
        self.time = time
        self.duration = duration
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self, time):
        if self.time <= time <= self.time + self.duration:
            game_display.blit(self.image, (self.pos_x, self.pos_y))

    def show_duration(self):
        self.draw(self.time)
        pygame.display.update()
        self.displayed = True
        clock.tick(1000 / self.duration)
        game_display.fill(BACKGROUND_COLOR)
        pygame.display.update()


def window_closed():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


class _Colors:
    black = (0, 0, 0)
    white = (255, 255, 255)


BACKGROUND_COLOR = _Colors.white
