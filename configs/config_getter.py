import configparser


class Authorise:
    def __init__(self):
        self.configs = configparser.ConfigParser()
        self.configs.read("configs/config.ini")

    @property
    def login(self):
        return self.configs["AUTHORISE"]["login"]

    @property
    def password(self):
        return self.configs["AUTHORISE"]["password"]
