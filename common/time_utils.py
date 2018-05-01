import time
from settings import Settings


def current_time_milli():
    return int(round(time.time() * 1000))


def time_elapsed_milli(start_time_milli):
    return current_time_milli() - start_time_milli


def milli_to_second(millis):
    return millis / 1000


def check_total_elapsed(start_time):
    return Settings.total_lifetime_seconds > milli_to_second(time_elapsed_milli(start_time))
