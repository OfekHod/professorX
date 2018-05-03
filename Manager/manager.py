import random
from datetime import datetime, timedelta
from uuid import uuid4
import os
import threading

from common.event import Event
from common.settings import Settings
from common.time_utils import check_total_elapsed, current_time_milli
# TODO import correct fucntion
from eeg.recorder import eeg_logic, Recorder
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
              image_path=os.path.join(Settings.images_path, image),
              uuid=uuid
              )
    )

    next_start_time = next_end_time + timedelta(seconds=WAIT_INTERVAL)
    next_end_time = next_start_time + timedelta(seconds=SHOW_TIME)

for event in events:
    print event

images_drawer = ImagesDrawer([ImageDisplay(event) for event in events])


def main(draw_func, fps=40):
    finish_time = events[-1].end_time + timedelta(seconds=WAIT_INTERVAL)

    start_time = current_time_milli()

    # TODO: start eeg
    recorder = Recorder(finish_time)
    recorder.start_recording_thread()

    # while check_total_elapsed(start_time) and not window_closed():
    while datetime.now() <= finish_time and not window_closed():
        # draw_func(current_time_milli() - start_time)
        draw_func(datetime.now())
        clock.tick(fps)

    # TODO: end eeg
    # TODO: edit data(add cluster_id)


main(images_drawer.draw)
