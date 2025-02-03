from .attacks import Attack, SpellAttack, EmptyAttack
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

    def attack(self) -> dict:
        return self.attacker.hit()

    def spell_attack(self) -> dict:
        # then remove (all the logic of strokes in the method <attack>)
        return self.spell_attacker.hit()

    def pass_battle(self) -> dict:
        return self.empty_attacker.hit()


