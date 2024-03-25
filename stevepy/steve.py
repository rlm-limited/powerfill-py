import logging
from controllers.charger import ChargeBoxController
from controllers.database import DBController
from controllers.ocpp_tag import OCPPTagController
from controllers.web import WebController
from controllers.transactions import TransactionsController


logger = logging.getLogger(__name__)


class SteveSDK:

    def __init__(self, steve_url : str, db_credentials : str, *args, **kwargs):
        try:
            self.database = DBController(database_url=db_credentials)
            self.chargerbox = ChargeBoxController(database=self.database)
            self.ocpp_tag = OCPPTagController(database=self.database)
            self.web = WebController(steve_url=steve_url)
            self.transactions = TransactionsController(database=self.database, steve_url=steve_url)
        except:
            raise ValueError()


