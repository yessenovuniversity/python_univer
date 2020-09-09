class Config:
    def __init__(self, host, name, user, password, port = 1433):
        self.host = host,
        self.port = port,
        self.name = name,
        self.user = user,
        self.password = password


config = None


def set_config(_config):
    config = _config