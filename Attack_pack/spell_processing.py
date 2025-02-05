import random

baffs: list[int] = [4, 7, 10, 19, 22]   # 22 ?
damages: dict[int: list] = {
    1: [1, 2, 3, 12, 15, 16, 18, 24],  # 16 - ?
    2: [14, 23, ],
    3: [5, 6, 9, 11, 20, ]  # 9 - на всех (уменьшение)
}


def get_type(spell_number: int) -> str:
    if spell_number in baffs: return "baff"
    return "damage"


def get_attacker_count(spell_number: int) -> int:
    if spell_number in damages[1]: return 1
    if spell_number in damages[2]: return 2
    if spell_number in damages[3]: return 3
    if spell_number not in baffs: print(f"ATTACK COUNT DONT FOUND: {spell_number}")
    return 0


class SpellChooser:
    """
    Класс для обработи имеющихся в наличии заклинаний и
    выбора одного для использования
    """

    def __init__(self):
        pass

    def _process(self, spells: list[dict]) -> list[dict]:

        processed_spells = []
        for spell in spells:
            processed_spells.append(
            {
                "number": spell["SpellType"],
                "type": get_type(spell["SpellType"]),
                "attackers_count": get_attacker_count(spell["SpellType"])
            })
        return processed_spells


    def choose(self, spells: list[dict]) -> int:
        """
        Выбирает одно из заклинаний

        :param spells: - список заклинаний
        :return: номер выбранного заклинания
        """

        spells = self._process(spells=spells)

        return spells[random.randint(0, len(spells))-1]["number"]

