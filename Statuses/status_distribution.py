import requests
from .wait import Waiting
from .towers_of_the_magic import TowersBattle
from ._abstract_status_class import Status


class StatusDistribution:
    """ ... """
    def __init__(self ,session: requests.Session):
        self.session = session

    def distributing(self, status: dict[str: bool]) -> Status:
        """ ... """

        if status["clan_tournament"]:
            pass
        if status["tournament_1_of_5"]:
            pass
        if status["tournament_1_of_1"]:
            pass
        if status["invasion"]:
            pass
        if status["towers_battlse"]:
            print('\rсобытие: Башни магии')
            return TowersBattle(self.session)

        if status["colosseum_of_the_Gods"]:
            pass
        if status["clan_tournament_1_of_5"]:
            pass

        return Waiting()
