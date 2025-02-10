import json
import datetime


"""
the information looks like this:

{
    "date": str,
    "daly_tasks_completed": bool,
    "chaos_arena_played": int
}


"""

class StatusController:
    def __init__(self):
        self.status = GameStatus()

    def update_info(self):
        date = self.status._get_date_today()
        last_date = self.status.get_last_date()
        if date != last_date:
            self.status.update_date(date=date)
            self.status.reset()



class GameStatus:

    def __init__(self):
        self.status_file_path: str = "game_status/game_status.json"
        self.status: dict ={}

    def _open_file(self):
        with open(self.status_file_path, 'r', encoding='utf-8') as file:
            self.status = json.load(file)

    def _save_satus(self):
        with open(self.status_file_path, 'w', encoding='utf-8') as file:
            json.dump(self.status, file)

    def _get_date_today(self):
        date = datetime.datetime.now()
        return f"{date.day}.{date.month}.{date.year}"

    def get_last_date(self):
        self._open_file()
        return self.status["date"]


    def reset(self):
        self.update_date(date=self._get_date_today())
        self._open_file()
        self.status["daly_battles_completed"] = False
        self.status["daly_treasury_replenishment"] = False
        self.status["chaos_arena_played"] = 0
        self._save_satus()

    def update_date(self, date: str):
        self._open_file()
        self.status["date"] = date
        self._save_satus()

    def complite_daily_battkes(self):
        self._open_file()
        self.status["daly_battles_completed"] = True
        self._save_satus()

    def complite_daily_battkes(self):
        self._open_file()
        self.status["daly_treasury_replenishment"] = True
        self._save_satus()

    def add_chaos_arena_battle(self):
        self._open_file()
        self.status["chaos_arena_played"] += 1
        self._save_satus()
