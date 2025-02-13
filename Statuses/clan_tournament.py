from ._abstract_status_class import Status
import requests


class ClanTournament(Status):
    """ ... """

    def __init__(self ,session: requests.Session):
        self.session = session

    def run(self):
        """ ... """
        pass




"""

https://magi.mobi/clans_tournament_async/join  --  get  --  присоединиться к турниру

https://magi.mobi/clans_tournament_async  -- get -- поиск токена

4й <timer-element>  в  data-timer-repeat-action

https://magi.mobi/clans_tournament_async/players_count?format=json  -- get  -- получения статуса для начала
{"PlayersCount":1356, "Started":true}  --  смотрим на Started


https://magi.mobi/json/clans_tournament_async/battle_request  -- post  -- удар (?)

PlayerGuid: 16eca149-f29c-4c87-a048-ee31229d92db
BattleRequestType: 1

status:
    1 - 
    2 - 
    3 - 


https://magi.mobi/json/tournament/check_state?format=json  -- post  -- проверка пока ждешь бой
['RoundInfoJson']['Active']  -- true  /  false

либо

['Status']  true - ожидание // false - начало боя



https://magi.mobi/clans_tournament_async/clan_status/16eca149-f29c-4c87-a048-ee31229d92db?format=json  --  get  --  после смерти
['Active']  false - бой окончен



по окончанию турнира  --  https://magi.mobi/json/tournament/check_state?format=json  --  post  --  возвращает:

{"ViewedLeague":"Master","Status":true}

напостоянку. get_info  дает в статусе false. Решить

"""