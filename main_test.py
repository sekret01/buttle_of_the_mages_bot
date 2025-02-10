from session import start_session
from Battles import ChaosArena, TowersBattle
from status_monitoring import StatusMonitor
from game_status import StatusController


session = start_session()

# tb = TowersBattle(session=session)
# tb.play_tournament()

# ca = ChaosArena(session=session)
# ca.play_round()

# monitor = StatusMonitor(session=session)
# print(monitor.update_status())


s = StatusController()
print("date")
print(s.reset())
