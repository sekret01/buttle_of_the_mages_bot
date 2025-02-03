from attacks import Attack, SpellAttack


class AttackController:
    """ ... """
    def __init__(self, session: requests.Session, guit: str, battle_type: str):
        self.attacker = Attack(session, guit, battle_type)
        self.spell_attacker = SpellAttack(session, guit, battle_type)

    def attack():
        self.attacker.hit()

    def spell_attack():
        self.spell_attacker.hit()
