from .attacks import Attack, SpellAttack, EmptyAttack
from .spell_processing import SpellChooser
import requests


def get_api_to_battle_type(battle_type):
    apis = {
        "chaos_arena": "arena_async",
        "towers_of_the_mages": "mobasix"
    }
    return apis[battle_type]


class AttackController:
    """ ... """
    def __init__(self, session: requests.Session, guit: str, battle_type: str):
        battle_type_api = get_api_to_battle_type(battle_type=battle_type)
        self.attacker = Attack(session, guit, battle_type_api)
        self.spell_attacker = SpellAttack(session, guit, battle_type_api)
        self.empty_attacker = EmptyAttack(session, guit, battle_type_api)
        self.spell_chooser = SpellChooser()  # NEW

    def attack(self) -> dict:
        resp = self.attacker.hit()

        spells = []
        spells += resp["PlayerInfo"]["SpellsInfo"]
        if "BookSpellInfo" in resp["PlayerInfo"].keys():
            spells.append(resp["PlayerInfo"]["BookSpellInfo"])
        if "ClanBookSpellInfo" in resp["PlayerInfo"].keys():
            spells.append(resp["PlayerInfo"]["ClanBookSpellInfo"])

        spell_number: int = self.spell_chooser.choose(spells=spells)

        self.spell_attacker.hit(spell_number=spell_number)
        return resp

    def spell_attack(self) -> dict:
        # then remove (all the logic of strokes in the method <attack>)
        return self.spell_attacker.hit()

    def pass_battle(self) -> dict:
        return self.empty_attacker.hit()

    def go_to_tower(self) -> dict:
        return self.attacker.go_to_tower()


