from ._abstract_status_class import Status
import requests


class Tournament_1vs1(Status):
    """ ... """

    def __init__(self ,session: requests.Session):
        self.session = session

    def run(self):
        """ ... """
        pass
    