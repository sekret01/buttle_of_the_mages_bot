from session import start_session
from Battles import ChaosArena, TowersBattle

session = start_session()
# tb = TowersBattle(session=session)
# tb.play_tournament()

ca = ChaosArena(session=session)
ca.play_round()

