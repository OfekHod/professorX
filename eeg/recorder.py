import json
import random
import time
import uuid

from datetime import datetime
from mindcontrol.userbrain import Brain
from time import sleep

import matplotlib.pyplot as plt

import plotter


def eeg_logic():
    pass


class Recorder(object):
    SLEEP_TIME = 5  # seconds
    CONCENTRATE_TIME = 5  # seconds

    def __init__(self, finish_time):
        self.finish_time = finish_time
        self.my_brain = Brain()
        while not self.my_brain.isConnected():
            print 'Not connected to brain yet. Will try again in %d seconds' % self.SLEEP_TIME
            sleep(self.SLEEP_TIME)
        self.conc_vals = []
        plt.axis([0, 100, 0, 100])

        self.total_values = {
            "lowGamma": [100000, 0],
            "highGamma": [100000, 0],
            "highAlpha": [100000, 0],
            "delta": [100000, 0],
            "highBeta": [100000, 0],
            "lowAlpha": [100000, 0],
            "lowBeta": [100000, 0],
            "theta": [100000, 0],
        }

    @staticmethod
    def update_range_values(abs_values, given_data):
        for wave_type in abs_values:
            if abs_values[wave_type][0] >= given_data[wave_type]:
                abs_values[wave_type][0] = given_data[wave_type]
            if abs_values[wave_type][1] <= given_data[wave_type]:
                abs_values[wave_type][1] = given_data[wave_type]
        return abs_values

    def start_recording(self):
        # random_clusters = [str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())]
        # is_correct_answer_values = [1, 0, 0]
        init_time = time.time()

        total_data = []
        while datetime.now() <= self.finish_time:
            self.conc_vals.append(self.my_brain.getProperty('attention'))
            current_data = self.my_brain.freshest_data

            current_data["time"] = str(time.time() - init_time)

            # current_data["cluster_id"] = random_clusters[fixed_values_index]
            # current_data["is_correct"] = is_correct_answer_values[fixed_values_index]

            total_data.append(current_data)

            x = time.time() - init_time
            plt.scatter(x, int(self.my_brain.freshest_data['attention']))

            if int(time.time() - init_time) % 10 == 0:
                print "recorder is running"

            plt.pause(0.05)
            sleep(0.1)

        # plotter.plot(total_data)


# recorder = Recorder()
# recorder.start_recording()
