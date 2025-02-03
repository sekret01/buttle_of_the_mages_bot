"""
Attack classes.
The attack is divided into 
  - hit
  - spell

"""

import requests


class Attack:
    """ ... """

    def __init__(self, session: requests.Session, guit: str, battle_type: str) -> None:
        """ ... """
        self.url = f"https://magi.mobi/json/{battle_type}/battle_request"
        self.session = session
        self.guit: str = guit
        self.hit_type: int = 1
    
    def hit(self) -> dict:
        """ ... """
        request_data = {
            "BattleRequestType": self.hit_type,
            "PlayerGuid": self.guit
        }
        hit_resp = self.session.post(url=self.url, data=request_data)
        return hit_resp.json()


class EmptyAttack(Attack):
    def __init__(self, session: requests.Session, guit: str, battle_type: str):
        super().__init__(session, guit, battle_type)

    def hit(self) -> dict:
        """ ... """
        request_data = {
            "PlayerGuid": self.guit
        }
        hit_resp = self.session.post(url=self.url, data=request_data)
        return hit_resp.json()


class SpellAttack(Attack):
    """ ... """
    def __init__(self, session: requests.Session, guit: str, battle_type: str):
        super().__init__(session, guit, battle_type)
        self.hit_type: int = 2
        self.spell_info: dict = {}

    def hit(self) -> dict:
        """ ... """
        request_data = {
            "BattleRequestType": self.hit_type,
            "PlayerGuid": self.guit,
            # ...
        }
        hit_resp = self.session.post(url=self.url, data=request_data).json()
        return hit_resp.json()
