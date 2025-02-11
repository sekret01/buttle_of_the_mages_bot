from status_monitoring import StatusMonitor
from game_status import StatusController
from Statuses import ChaosArena, DailyAffairs, StatusDistribution
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
        self.status_distributor = StatusDistribution(session=session)

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
            event = self.status_distributor.distributing(status=status)
            event.run()
