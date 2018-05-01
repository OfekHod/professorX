import pygame

from images_drawer import game_display


class ImageDisplay(object):
    displayed = False

    def __init__(self, event, pos_x=0, pos_y=0):
        """
        :param common.event.Event event: event object to use
        :param int pos_x:
        :param int pos_y:
        """
        self.image = pygame.image.load(event.image_path)
        self.start_time = event.start_time
        self.end_time = event.end_time
        self.pos_x = pos_x
        self.pos_y = pos_y

    # Draw image if given time is inside duration window.
    def draw(self, display_time):
        if self.start_time <= display_time <= self.end_time:
            game_display.blit(self.image, (self.pos_x, self.pos_y))