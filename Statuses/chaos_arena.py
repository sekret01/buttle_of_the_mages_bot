import time
import requests
from bs4 import BeautifulSoup
from Attack_pack import AttackController



class ChaosArena:
    """ ... """

    def __init__(self, session):
        self.session: requests.Session = session
        self.battle_type: str = "chaos_arena"
        self.wait_guit: str = ""
        self.battle_guit: str = ""

    def run(self, loose: bool = False):
        """ one round in the chaos arena (full cycle) """

        self.session.get("https://magi.mobi/arena_async/enter")
        wait_guit = self._get_waiting_guit()
        if wait_guit is None:
            return
        self.wait_guit = wait_guit
        self._wait_for_battle()
        self.battle_guit = self._get_battle_guit()
        time.sleep(1)
        self._battle(loose=loose)
        self._get_price()

    def _get_waiting_guit(self) -> str | None:
        """  ... """

        # time.sleep(3)
        resp = self.session.get("https://magi.mobi/arena_async")
        soup = BeautifulSoup(resp.text, 'html.parser')
        data = soup.find_all("timer-element")
        if len(data) == 3:
            player_guid = data[1]['data-timer-repeat-action']
            player_guid = player_guid.split('?')[0].split('/')[-1]
            print(player_guid)
            return player_guid
        print("не удалось получить код")
        return None

    def _get_battle_guit(self) -> str:
        """ ... """
        resp = self.session.get("https://magi.mobi/arena_async")
        soup = BeautifulSoup(resp.text, 'html.parser')
        player_guid = soup.find("battle-phaser-init")['player-guid']
        return player_guid

    def _wait_for_battle(self):
        i: int = 0
        while i < 30:
            time.sleep(1.5)
            battle_data = self.session.get(f"https://magi.mobi/json/arena_async/battle_status/{self.wait_guit}?format=json").json()
            if battle_data['PlayersCount'] == battle_data["PlayersMax"]:
                return
        print("Время ожидания превышено")

    def _battle(self, loose) -> None:
        attacker = AttackController(session=self.session,
                                    guit=self.battle_guit,
                                    battle_type=self.battle_type)
        if loose:
            while attacker.pass_battle()["Status"]:
                time.sleep(5)
            return

        total = "Победа"
        while True:
            resp = attacker.attack()
            if resp['PlayerInfo']['Params']['CurrentHealth'] == 0:
                total = "Игрок был убит"

            elif resp['EnemiesCount'] == 0:
                print(total)
                return

            elif resp['Status'] is False:
                print(total)
                print("Битва окончена")
                return
            time.sleep(0.8)

    def _get_price(self):
        self.session.get("https://magi.mobi/arena_async/result_confirm")

