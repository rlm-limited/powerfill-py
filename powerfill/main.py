import logging


logger = logging.getLogger(__name__)


class PowerfillSDK:

    def __init__(self, endpoint: str, port: int, username: str, password: str, *args, **kwargs):
        self.endpoint = endpoint
        self.port = port
        self.username = username
        self.password = password
        
        


