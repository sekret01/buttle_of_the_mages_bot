import json


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
        self.status_file_path: str = "game_status/game_status.json"
        self.status: dict ={}

    def _open_file(self):
        with open(self.status_file_path, 'r', encoding='utf-8') as file:
            self.status = json.load(file)

    def _save_satus(self):
        with open(self.status_file_path, 'w', encoding='utf-8') as file:
            json.dump(self.status, file)

    def update_date(self, date: str):
        self._open_file()
        self.status["date"] = date
        self._save_satus()

    ...
