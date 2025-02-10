import json
import datetime


"""
the information looks like this:

{
    "date": "10.2.2025",
    "daly_battles_completed": false,
    "daily_treasury_replenishment": false,
    "chaos_arena_played": 0
}


"""


class StatusController:

    def __init__(self):
        self.status_file_path: str = "game_status/game_status.json"
        self.status: dict = {}

    def _open_file(self):
        with open(self.status_file_path, 'r', encoding='utf-8') as file:
            self.status = json.load(file)

    def _save_satus(self):
        with open(self.status_file_path, 'w', encoding='utf-8') as file:
            json.dump(self.status, file)

    def _get_date_today(self):
        date = datetime.datetime.now()
        return f"{date.day}.{date.month}.{date.year}"
    
    
    def update_info(self) -> bool:
        date = self._get_date_today()
        last_date = self.get_last_date()
        if date != last_date:
            self.update_date(date=date)
            return True
        return False

    def get_last_date(self):
        self._open_file()
        return self.status["date"]

    def update_date(self, date: str):
        self._open_file()
        self.status["date"] = date
        self._save_satus()

    def get_status(self):
        self._open_file()
        return self.status
