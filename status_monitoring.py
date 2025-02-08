import requests


class StatusMonitor:
    """ monitors the status of current events """

    def __init__(self, session: requests.Session):
        """ ... """
        self.session: requests.Session = session

    def update_status(self) -> dict[str: bool]:
        """
        method to get the current status of events.

        example return value:
            {
                'clan_tournament': True,
                'tournament_1_of_5': False,
                'tournament_1_of_1': False,
                'invasion': False,
                'towers_battlse': False,
                'colosseum_of_the_Gods': False,
                'clan_tournament_1_of_5': False
            }


        :return: dictionary with status values like: <event_name>: <bool>
        
        """
        
        res = self.session.post("https://magi.mobi/home/get_info").json()
        battles_status = res["TournamentInfos"]

        status = {
            "clan_tournament": battles_status[0]["Active"],
            "tournament_1_of_5": battles_status[1]["Active"],
            "tournament_1_of_1": battles_status[2]["Active"],
            "invasion": battles_status[3]["Active"],
            "towers_battlse": battles_status[4]["Active"],
            "colosseum_of_the_Gods": battles_status[5]["Active"],
            "clan_tournament_1_of_5": battles_status[6]["Active"]

        }

        return status
