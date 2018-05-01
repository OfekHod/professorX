import random
from datetime import datetime, timedelta
from uuid import uuid4
import os

from common.event import Event
from common.settings import Settings
from common.time_utils import check_total_elapsed, current_time_milli
from eeg.eeg import eeg_logic
from view.image_display import ImageDisplay
from view.images_drawer import ImagesDrawer, window_closed, clock


# IMAGES = ['january.png', 'february.png', 'march.png']
IMAGES = ['nadav.jpg', 'hen.jpg', 'prof1.jpg']

WAIT_INTERVAL = 1.5  # seconds
SHOW_TIME = 0.2  # seconds

uuid_to_image = {}

random_ordered_images = IMAGES[:]
random.shuffle(random_ordered_images)

events = []
absolute_start = datetime.now() + timedelta(seconds=WAIT_INTERVAL)
next_start_time = absolute_start
next_end_time = absolute_start + timedelta(seconds=SHOW_TIME)

for image in random_ordered_images:
    uuid = str(uuid4())
    uuid_to_image[uuid] = image

    events.append(
        Event(start_time=next_start_time,
              end_time=next_end_time,
              image_path=os.path.join(Settings.images_path,image),
              uuid=uuid
              )
    )

    next_start_time = next_end_time + timedelta(seconds=WAIT_INTERVAL)
    next_end_time = next_start_time + timedelta(seconds=SHOW_TIME)

for event in events:
    print event

images_drawer = ImagesDrawer([ImageDisplay(event) for event in events])


def main_loop(update, draw_func, fps=40):
    start_time = current_time_milli()

    while check_total_elapsed(start_time) and not window_closed():
        update()
        # draw_func(current_time_milli() - start_time)
        draw_func(datetime.now())
        clock.tick(fps)


main_loop(eeg_logic, images_drawer.draw)
