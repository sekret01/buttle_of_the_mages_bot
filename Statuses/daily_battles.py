import requests


class DailyAffairs:
    def __init__(self, session: requests.Session):
        self.session = session
        self.urls = {
            'daily_prize': "https://magi.mobi/dailyprize/getprize/",
            'towers_resources': "https://magi.mobi/tower/gatherajax?format=json",
            'auto_battle_company': "https://magi.mobi/home/bosses_auto_fight",
            'auto_battle_portals': "https://magi.mobi/plist/pass",
            'skip_time': "https://magi.mobi/home/start",
            'battle_all': "https://magi.mobi/do_all/do"
        }

    def take_daily_prize(self):
        self.session.get(self.urls['daily_prize'])

    def daily_mobs_battle(self):
        for i in range(2):
            self.session.post(self.urls['towers_resources'])
            self.session.get(self.urls['auto_battle_company'])
            self.session.get(self.urls['auto_battle_portals'])
            if i < 1: self.session.get(self.urls['skip_time'])
        
        for _ in range(2):
            self.session.get(self.urls['battle_all'])

    def perform_tasks(self):
        self.session.get("https://magi.mobi/quests/reward/winboss/233")
        self.session.get("https://magi.mobi/quests/reward/winportals/231")
        self.session.get("https://magi.mobi/quests/reward/gatherallgoldfromtower/232")

    def replenish_the_treasury(self):
        """ Replenishment of the clan treasury for 10 coins """

        self.session.post(url="https://magi.mobi/clan/treasures",
                    data={"Gold": 10})
        

