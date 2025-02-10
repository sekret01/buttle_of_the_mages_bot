from status_monitoring import StatusMonitor
from game_status import StatusController
from Battles import ChaosArena, TowersBattle, DailyAffairs
import threading
import time
import datetime
import requests


class TaskDistributor:
    """ ... """

    def __init__(self, session: requests.Session):
        self.session = session
        self.monitor = StatusMonitor(session=session)
        self.status_controller = StatusController()

    def run(self):
        """ ... """
        while True:

            is_new_day = self.status_controller.update_info()
            
            if is_new_day:
                print(f"Обновление дня...")
                daily_affairing = DailyAffairs(self.session)
                daily_affairing.take_daily_prize()
                daily_affairing.daily_mobs_battle()
                daily_affairing.replenish_the_treasury()
                daily_affairing.perform_tasks()

                del daily_affairing
                print("Ежеждневные задания выполнены\n")


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
