from view.images_drawer import ImagesDrawer, clock, window_closed, image
from view.image_display import ImageDisplay
from common.time_utils import current_time_milli, check_total_elapsed
from eeg.recorder import eeg_logic

start_time = current_time_milli()


# Assuming frame duration is faster than desired image display duration.
# Consider use update() in another thread pool if eeg calls takes long time.
def main_loop(update, draw, fps=40):
    while check_total_elapsed(start_time) and not window_closed():
        update()
        draw(current_time_milli() - start_time)
        clock.tick(fps)


main_loop(update=eeg_logic,
          draw=drawer.draw)

quit()
