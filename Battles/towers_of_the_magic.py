import requests
import time
from requests import session
from Attack_pack import AttackController
from bs4 import BeautifulSoup



class TowersBattle:
    """ A full cycle of battle <towers of magic> """
    def __init__(self, session: requests.Session):
        self.session: requests.Session = session
        self.battle_type: str = "towers_of_the_mages"
        self.guit: str = "746e968d-9358-40c3-aadc-28aa6185f525"

    def play_tournament(self):
        """ ... """

        self._join_tournament()
        self.guit = self._get_guit()
        if self.guit == "": return
        self._wait_for_battle()
        self._battle()


    def _join_tournament(self) -> None:
        resp = self.session.post("https://magi.mobi/mobasix/join")
        print(f"Подключение к турниру: {resp.status_code}")

    def _get_guit(self) -> str:
        """ ... """

        time.sleep(1)
        resp = self.session.get("https://magi.mobi/mobasix")
        soup = BeautifulSoup(resp.text, 'html.parser')
        if soup is None:
            print("Страница не найдена")
            return ""

        print("Страница обнаружена")

        data = soup.find_all("timer-element")
        print("объектов timer: ",len(data))
        if len(data) > 3:
            player_guid = data[3]['data-timer-repeat-action']
            player_guid = player_guid.split("'")[1].split('/')[-1]
            print(player_guid)
            return player_guid
        print("не удалось получить код")
        return ""

    def _wait_for_battle(self) -> None:
        while True:
            time.sleep(1)
            battle_data = self.session.post(f"https://magi.mobi/home/get_info").json()
            left_time = battle_data['TournamentInfos'][4]['SecondsLeft']
            print(f"\rВремени до начала: {left_time}", end='')
            if left_time < 10:
                print('\nожидание начала (80 сек)')
                time.sleep(80)
                return

    def _battle(self):
        attacker = AttackController(
            session=self.session,
            guit=self.guit,
            battle_type=self.battle_type
        )

        print("Начало битвы")

        while True:
            resp = attacker.attack()
            left_time = resp['TimeLeft']
            print(f'\rДо конца: {left_time}', end='')
            time.sleep(1.5)

            if resp['BattleData']['ShowCommand']:
                self._accept_command()
                attacker.go_to_tower()

            if not resp["BattleData"]["IsTargetTower"]:
                attacker.go_to_tower()

            if int(left_time.split(':')[1]) < 2 and int(left_time.split(':')[0]) == 0:
                print("\n\nТурнир окончен")
                return

    def _accept_command(self):
        try:
            self.session.get(f"https://magi.mobi/json/moba/accept_command/{self.guit}")
        except Exception as ex:
            print(f"\n\nОШИБКА\n{ex}\n")
