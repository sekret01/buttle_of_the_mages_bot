from Attack_pack import AttackController
from configs import Authorise
from session import start_session
from chaos_arena import ChaosArena

session = start_session()
ca = ChaosArena(session=session)
ca.play_round()

