from ._abstract_status_class import Status
import time


class Waiting(Status):
    """ ... """
    def __init__(self):
        pass

    def run(self):
        time.sleep(60 * 5)
