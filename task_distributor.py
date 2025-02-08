from status_monitoring import StatusMonitor
from Battles import ChaosArena, TowersBattle
import threading
import time
import datetime
import requests


class TaskDistributor:
    """ ... """

    def __init__(self, session: requests.Session):
        self.session = session
        self.monitor = StatusMonitor(session=session)

    def run(self):
        """ ... """
        while True:
            print('\rожидание событий...', end='')

            status = self.monitor.update_status()
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
                towers_battle = TowersBattle(self.session)
                towers_battle.play_tournament()

            if status["colosseum_of_the_Gods"]:
                pass
            if status["clan_tournament_1_of_5"]:
                pass

            time.sleep(60*5)
