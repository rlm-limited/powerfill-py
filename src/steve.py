import logging
from controllers.charger import ChargeBoxController
from controllers.database import DBController
from controllers.ocpp_tag import OCPPTagController
from controllers.web import WebController
from controllers.transactions import TransactionsController


from pyinstrument import Profiler



logger = logging.getLogger(__name__)


class SteveSDK:

    def __init__(self, steve_url : str, db_credentials : str, *args, **kwargs):
        try:
            self.database = DBController(database_url=db_credentials)
            self.chargerbox = ChargeBoxController(database=self.database)
            self.ocpp_tag = OCPPTagController(database=self.database)
            self.web = WebController(steve_url=steve_url)
            self.transactions = TransactionsController(database=self.database, steve_url=steve_url, chargebox=self.chargerbox, ocpp_tag=self.ocpp_tag)
        except:
            raise ValueError()



if __name__ == '__main__':
    profiler = Profiler()
    profiler.start()

    steve = SteveSDK(steve_url='http://ev.meshpower.co.rw:8180/', db_credentials="mariadb+mariadbconnector://steve:changeme@ev.meshpower.co.rw:3306/stevedb")


    #view all ocpp tags
    #all_tags = steve.ocpp_tag.get_all_tags()

    #tag_with_id = steve.ocpp_tag.get_tag_with_id(id_tag="078jndfd")

    #new_tag = steve.ocpp_tag.create_tag(id_tag=94783089337)

    #n_tag = steve.ocpp_tag.get_or_create_tag(id_tag=93583089337)


    #view all chargeboxes
    #chargers = steve.chargerbox.get_all_chargeboxes()

    #chargebox = steve.chargerbox.get_charge_box_with_id(charge_box_id="633150404")

    #status = steve.chargerbox.get_connector_status_with_chargebox_id(charge_box_id="633150404", connector_id=1)

    #codes end here


    all_transactions = steve.transactions.get_all_transactions()

    start_transaction = steve.transactions.remote_start(charge_box_id="633150404", connector_id=1, id_tag="94783089337")

    profiler.stop()
    profiler.print()
    profiler.write_html("bingo.html")
