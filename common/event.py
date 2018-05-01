class Event(object):
    def __init__(self, start_time, end_time, image_path, uuid):
        self.start_time = start_time
        self.end_time = end_time
        self.image_path = image_path
        self.uuid = uuid

    def __repr__(self):
        return "{image} from {start} to {end}, with uuid of: {uuid}".format(
            image=self.image_path, start=self.start_time, end=self.end_time, uuid=self.uuid)