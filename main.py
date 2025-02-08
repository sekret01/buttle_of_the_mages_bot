from task_distributor import TaskDistributor
from session import start_session


def main() -> None:

    session = start_session()
    print("[*] начало прослушивания\n")

    distributor = TaskDistributor(session)

    distributor.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
