from view import ImagesDrawer, ImageDisplay, clock, window_closed
from utils import current_time_milli, image, check_total_elapsed

drawer = ImagesDrawer([
    ImageDisplay(image("prof1.jpg"), 1000, 1500, -100),
    ImageDisplay(image("nadav.jpg"), 3000, 200, 50),
    ImageDisplay(image("hen.jpg"), 3700, 400, 50),
    ImageDisplay(image("nadav.jpg"), 4600, 250, 50),
    ImageDisplay(image("hen.jpg"), 5250, 50, 50)])

start_time = current_time_milli()


# Assuming frame duration is faster than desired image display duration.
# Consider use update() in another thread pool if eeg calls takes long time.
def main_loop(update, draw, fps=40):
    while check_total_elapsed(start_time) and not window_closed():
        update()
        draw(current_time_milli() - start_time)
        clock.tick(fps)


def eeg_logic(): return


main_loop(update=eeg_logic,
          draw=drawer.draw)

quit()
