from configs import Authorise
import requests
import sys


def _authorise(session) -> bool:
    """ ... """
    auth_data = Authorise()
    login = auth_data.login
    password = auth_data.password

    link = f"https://magi.mobi/auth/credentials?Continue=/profile&UserName={login}&Password={password}"
    if session.post(link).status_code == 200:
        try:
            resp = session.get("https://magi.mobi/chat/new_messages/1?format=json").json()
            print(f"Вход совершен\n"
                  f"игрок: {resp['CurrentPlayerName']}\n"
                  f"id: {resp['CurrentPlayerId']}")
            return True
        except Exception as ex:
            print("Попытка входа не удалась")
            print(ex)
    else:
        print("Запрос был обработан некорректно")
    return False


def start_session() -> requests.Session:
    """ ... """
    
    session = requests.Session()
    session.headers.update(
        {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"',
            "accept-encoding": "UTF-8",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "accept": "*/*"
        }
    )
    if _authorise(session=session):
        return session
    sys.exit()
