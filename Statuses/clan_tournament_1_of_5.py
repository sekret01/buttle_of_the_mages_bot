from ._abstract_status_class import Status
import requests


class ClanTournament_1vs5(Status):
    """ ... """

    def __init__(self ,session: requests.Session):
        self.session = session

    def run(self):
        """ ... """
        pass